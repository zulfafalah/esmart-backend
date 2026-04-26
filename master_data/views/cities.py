from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from legacy.models import Mtcity
from master_data.serializers.cities import CityDetailSerializer
from master_data.serializers.cities import CityListSerializer
from master_data.serializers.cities import CityWriteSerializer


class CityListCreateView(APIView):
    """
    List all cities with pagination & search, or create a new one.
    Cities are stored in `mtcity` where `coa10 != 0`.
    """

    @extend_schema(
        summary="List cities",
        tags=["Cities"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="page_size", type=int, description="Items per page (default: 20)"),
            OpenApiParameter(name="search", type=str, description="Search by city name"),
            OpenApiParameter(
                name="ordering",
                type=str,
                description="Order results (e.g. cityname, -cityname)",
            ),
        ],
        responses={200: CityListSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        page_size = max(1, min(100, int(request.query_params.get("page_size", 20))))
        search = request.query_params.get("search", "").strip()
        ordering = request.query_params.get("ordering", "cityid").strip()

        # Cities: coa10 is not 0 (countries have coa10=0)
        qs = Mtcity.objects.using("esmart").exclude(coa10=0)

        if search:
            qs = qs.filter(Q(cityname__icontains=search))

        # Validate ordering field to prevent injection
        allowed_ordering_fields = {"cityid", "cityname", "bunitid", "created", "modified"}
        order_field = ordering.lstrip("-")
        if order_field not in allowed_ordering_fields:
            ordering = "cityid"

        qs = qs.order_by(ordering)

        total = qs.count()
        offset = (page - 1) * page_size
        qs = qs[offset : offset + page_size]

        serializer = CityListSerializer(qs, many=True)

        base_url = request.build_absolute_uri(request.path)
        next_page = (
            f"{base_url}?page={page + 1}&page_size={page_size}"
            if offset + page_size < total
            else None
        )
        prev_page = (
            f"{base_url}?page={page - 1}&page_size={page_size}"
            if page > 1
            else None
        )

        return Response(
            {
                "count": total,
                "next": next_page,
                "previous": prev_page,
                "results": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Create city",
        tags=["Cities"],
        request=CityWriteSerializer,
        responses={201: CityDetailSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = CityWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        instance = Mtcity.objects.using("esmart").create(
            cityname=validated_data["cityname"],
            citycountry="",
            coa10=validated_data["bunitid"],  # non-zero marks record as a City
            bunitid=validated_data["bunitid"],
            created=now,
            createdby=user,
            modified=now,
            modifiedby=user,
        )

        return Response(
            CityDetailSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class CityDetailView(APIView):
    """
    Retrieve, update, or delete a single city by cityid.
    Ensures the record is a city (coa10 != 0).
    """

    def _get_object(self, pk: int) -> Mtcity:
        try:
            return Mtcity.objects.using("esmart").exclude(coa10=0).get(cityid=pk)
        except Mtcity.DoesNotExist:
            raise NotFound(detail="City not found.")

    @extend_schema(
        summary="Get city detail",
        tags=["Cities"],
        responses={200: CityDetailSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = CityDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update city (full)",
        tags=["Cities"],
        request=CityWriteSerializer,
        responses={200: CityDetailSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = CityWriteSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        instance.cityname = validated_data["cityname"]
        instance.bunitid = validated_data["bunitid"]
        instance.coa10 = validated_data["bunitid"]
        instance.modified = now
        instance.modifiedby = user

        instance.save(
            using="esmart",
            update_fields=["cityname", "bunitid", "coa10", "modified", "modifiedby"],
        )

        return Response(
            CityDetailSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Delete city",
        tags=["Cities"],
        responses={204: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.delete(using="esmart")
        return Response(status=status.HTTP_204_NO_CONTENT)
