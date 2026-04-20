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
from master_data.serializers.countries import CountryDetailSerializer
from master_data.serializers.countries import CountryListSerializer
from master_data.serializers.countries import CountryWriteSerializer


class CountryListCreateView(APIView):
    """
    List all countries with pagination & search, or create a new one.
    Countries are stored in `mtcity` where `coa10 = 0`.
    """

    @extend_schema(
        summary="List countries",
        tags=["Countries"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="limit", type=int, description="Items per page (default: 10)"),
            OpenApiParameter(name="search", type=str, description="Search by country name"),
        ],
        responses={200: CountryListSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        limit = max(1, min(100, int(request.query_params.get("limit", 10))))
        search = request.query_params.get("search", "").strip()

        qs = Mtcity.objects.using("esmart").filter(coa10=0).order_by("cityid")

        if search:
            qs = qs.filter(Q(cityname__icontains=search))

        total = qs.count()
        offset = (page - 1) * limit
        qs = qs[offset : offset + limit]

        serializer = CountryListSerializer(qs, many=True)
        return Response(
            {
                "data": serializer.data,
                "page": page,
                "limit": limit,
                "total": total,
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Create country",
        tags=["Countries"],
        request=CountryWriteSerializer,
        responses={201: CountryDetailSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = CountryWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        cityname = serializer.validated_data["cityname"]

        instance = Mtcity.objects.using("esmart").create(
            cityname=cityname,
            citycountry=cityname,  # same as cityname on insert
            coa10=0,               # marks record as a Country
            created=now,
            createdby=user,
            modified=now,
            modifiedby=user,
        )

        return Response(
            CountryDetailSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class CountryDetailView(APIView):
    """
    Retrieve, update, or delete a single country by id.
    Ensures the record is a country (coa10 = 0).
    """

    def _get_object(self, pk: int) -> Mtcity:
        try:
            return Mtcity.objects.using("esmart").get(cityid=pk, coa10=0)
        except Mtcity.DoesNotExist:
            raise NotFound(detail="Country not found.")

    @extend_schema(
        summary="Get country detail",
        tags=["Countries"],
        responses={200: CountryDetailSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = CountryDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update country",
        tags=["Countries"],
        request=CountryWriteSerializer,
        responses={200: CountryDetailSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = CountryWriteSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        cityname = serializer.validated_data["cityname"]
        instance.cityname = cityname
        instance.citycountry = cityname
        instance.modified = now
        instance.modifiedby = user

        instance.save(
            using="esmart",
            update_fields=["cityname", "citycountry", "modified", "modifiedby"],
        )

        return Response(
            CountryDetailSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Delete country",
        tags=["Countries"],
        responses={200: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.delete(using="esmart")
        return Response(
            {"message": "Country deleted successfully."},
            status=status.HTTP_200_OK,
        )
