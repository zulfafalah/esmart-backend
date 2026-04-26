from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from legacy.models import Mtregion
from master_data.serializers.regions import RegionDetailSerializer
from master_data.serializers.regions import RegionListSerializer
from master_data.serializers.regions import RegionWriteSerializer


class RegionListCreateView(APIView):
    """
    List all regions with pagination & search, or create a new one.
    Regions are stored in `mtregion` where `coa19 = 1`.
    """

    @extend_schema(
        summary="List regions",
        tags=["Regions"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="page_size", type=int, description="Items per page (default: 20)"),
            OpenApiParameter(name="search", type=str, description="Search by region name or code"),
            OpenApiParameter(
                name="ordering",
                type=str,
                description="Order results (e.g. regionname, -regionname)",
            ),
        ],
        responses={200: RegionListSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        page_size = max(1, min(100, int(request.query_params.get("page_size", 20))))
        search = request.query_params.get("search", "").strip()
        ordering = request.query_params.get("ordering", "regionid").strip()

        # Regions: coa19 = 1
        qs = Mtregion.objects.using("esmart").filter(coa19=1)

        if search:
            qs = qs.filter(Q(regionname__icontains=search) | Q(regioncode__icontains=search))

        # Validate ordering field to prevent injection
        allowed_ordering_fields = {"regionid", "regionname", "regioncode", "cityid", "created", "modified"}
        order_field = ordering.lstrip("-")
        if order_field not in allowed_ordering_fields:
            ordering = "regionid"

        qs = qs.order_by(ordering)

        total = qs.count()
        offset = (page - 1) * page_size
        qs = qs[offset : offset + page_size]

        serializer = RegionListSerializer(qs, many=True)

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
        summary="Create region",
        tags=["Regions"],
        request=RegionWriteSerializer,
        responses={201: RegionDetailSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = RegionWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        instance = Mtregion.objects.using("esmart").create(
            cityid=validated_data["cityid"],
            regioncode=validated_data["regioncode"],
            regionname=validated_data["regionname"],
            coa19=1,
            created=now,
            createdby=user,
            modified=now,
            modifiedby=user,
        )

        return Response(
            RegionDetailSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class RegionDetailView(APIView):
    """
    Retrieve, update, or delete a single region by regionid.
    Ensures the record is a region (coa19 = 1).
    """

    def _get_object(self, pk: int) -> Mtregion:
        try:
            return Mtregion.objects.using("esmart").filter(coa19=1).get(regionid=pk)
        except Mtregion.DoesNotExist:
            raise NotFound(detail="Region not found.")

    @extend_schema(
        summary="Get region detail",
        tags=["Regions"],
        responses={200: RegionDetailSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = RegionDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update region (full)",
        tags=["Regions"],
        request=RegionWriteSerializer,
        responses={200: RegionDetailSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = RegionWriteSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        instance.cityid = validated_data["cityid"]
        instance.regioncode = validated_data["regioncode"]
        instance.regionname = validated_data["regionname"]
        instance.modified = now
        instance.modifiedby = user

        instance.save(
            using="esmart",
            update_fields=["cityid", "regioncode", "regionname", "modified", "modifiedby"],
        )

        return Response(
            RegionDetailSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Delete region",
        tags=["Regions"],
        responses={204: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.delete(using="esmart")
        return Response(status=status.HTTP_204_NO_CONTENT)
