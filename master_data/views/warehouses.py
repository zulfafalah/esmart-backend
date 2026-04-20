from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from legacy.models import Mtwhs
from master_data.serializers.warehouses import WarehouseDetailSerializer
from master_data.serializers.warehouses import WarehouseListSerializer
from master_data.serializers.warehouses import WarehouseWriteSerializer


class WarehouseListCreateView(APIView):
    """
    List all warehouses with pagination & search, or create a new one.
    """

    @extend_schema(
        summary="List warehouses",
        tags=["Warehouses"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="limit", type=int, description="Items per page (default: 10)"),
            OpenApiParameter(name="search", type=str, description="Search by name, code, or location"),
        ],
        responses={200: WarehouseListSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        limit = max(1, min(100, int(request.query_params.get("limit", 10))))
        search = request.query_params.get("search", "").strip()

        qs = Mtwhs.objects.using("esmart").all().order_by("whsid")

        if search:
            qs = qs.filter(
                Q(whscode__icontains=search)
                | Q(whsname__icontains=search)
                | Q(whsloc__icontains=search)
            )

        total = qs.count()
        offset = (page - 1) * limit
        qs = qs[offset : offset + limit]

        serializer = WarehouseListSerializer(qs, many=True)
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
        summary="Create warehouse",
        tags=["Warehouses"],
        request=WarehouseWriteSerializer,
        responses={201: WarehouseDetailSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = WarehouseWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        validated_data["bunitid"] = 0
        validated_data["created"] = now
        validated_data["createdby"] = user
        validated_data["modified"] = now
        validated_data["modifiedby"] = user

        instance = Mtwhs.objects.using("esmart").create(**validated_data)

        return Response(
            WarehouseDetailSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class WarehouseDetailView(APIView):
    """
    Retrieve, update, or delete a single warehouse by id.
    """

    def _get_object(self, pk: int) -> Mtwhs:
        try:
            return Mtwhs.objects.using("esmart").get(whsid=pk)
        except Mtwhs.DoesNotExist:
            raise NotFound(detail="Warehouse not found.")

    @extend_schema(
        summary="Get warehouse detail",
        tags=["Warehouses"],
        responses={200: WarehouseDetailSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = WarehouseDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update warehouse",
        tags=["Warehouses"],
        request=WarehouseWriteSerializer,
        responses={200: WarehouseDetailSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = WarehouseWriteSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        for attr, value in serializer.validated_data.items():
            setattr(instance, attr, value)

        instance.modified = now
        instance.modifiedby = user

        update_fields = list(serializer.validated_data.keys()) + ["modified", "modifiedby"]
        instance.save(using="esmart", update_fields=update_fields)

        return Response(
            WarehouseDetailSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Delete warehouse",
        tags=["Warehouses"],
        responses={200: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.delete(using="esmart")
        return Response(
            {"message": "Warehouse deleted successfully."},
            status=status.HTTP_200_OK,
        )
