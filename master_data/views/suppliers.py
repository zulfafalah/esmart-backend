from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from legacy.models import Mtsupplier
from master_data.serializers.suppliers import SupplierDetailSerializer
from master_data.serializers.suppliers import SupplierListSerializer
from master_data.serializers.suppliers import SupplierWriteSerializer


def _generate_suppcode() -> str:
    """Generate the next supplier code in the format F001, F002, ..."""
    last = (
        Mtsupplier.objects.using("esmart")
        .filter(suppcode__isnull=False)
        .exclude(suppcode="")
        .order_by("-supplierid")
        .values_list("suppcode", flat=True)
        .first()
    )
    if last:
        try:
            prefix = "".join(c for c in last if c.isalpha()) or "F"
            num = int("".join(c for c in last if c.isdigit())) + 1
        except (ValueError, TypeError):
            prefix, num = "F", 1
    else:
        prefix, num = "F", 1
    return f"{prefix}{num:03d}"


class SupplierListCreateView(APIView):
    """
    List all suppliers with pagination & search, or create a new one.
    """

    @extend_schema(
        summary="List suppliers",
        tags=["Suppliers"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="limit", type=int, description="Items per page (default: 10)"),
            OpenApiParameter(name="search", type=str, description="Search by company name, code, or contact name"),
        ],
        responses={200: SupplierListSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        limit = max(1, min(100, int(request.query_params.get("limit", 10))))
        search = request.query_params.get("search", "").strip()

        qs = Mtsupplier.objects.using("esmart").all().order_by("supplierid")

        if search:
            qs = qs.filter(
                Q(companyname__icontains=search)
                | Q(suppcode__icontains=search)
                | Q(contactname__icontains=search)
            )

        total = qs.count()
        offset = (page - 1) * limit
        qs = qs[offset : offset + limit]

        serializer = SupplierListSerializer(qs, many=True)
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
        summary="Create supplier",
        tags=["Suppliers"],
        request=SupplierWriteSerializer,
        responses={201: SupplierDetailSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = SupplierWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data

        # Auto-generate supplier code
        validated_data["suppcode"] = _generate_suppcode()

        # System defaults (not from request)
        validated_data["currencyid"] = "RP"
        validated_data["isactive"] = 1
        validated_data["created"] = now
        validated_data["createdby"] = user
        validated_data["modified"] = now
        validated_data["modifiedby"] = user

        # region field in model is CharField — store as string
        if "region" in validated_data and validated_data["region"] is not None:
            validated_data["region"] = str(validated_data["region"])

        instance = Mtsupplier.objects.using("esmart").create(**validated_data)

        return Response(
            SupplierDetailSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class SupplierDetailView(APIView):
    """
    Retrieve, update, or delete a single supplier by id.
    """

    def _get_object(self, pk: int) -> Mtsupplier:
        try:
            return Mtsupplier.objects.using("esmart").get(supplierid=pk)
        except Mtsupplier.DoesNotExist:
            raise NotFound(detail="Supplier not found.")

    @extend_schema(
        summary="Get supplier detail",
        tags=["Suppliers"],
        responses={200: SupplierDetailSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = SupplierDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update supplier",
        tags=["Suppliers"],
        request=SupplierWriteSerializer,
        responses={200: SupplierDetailSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = SupplierWriteSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        for attr, value in serializer.validated_data.items():
            # region field in model is CharField
            if attr == "region" and value is not None:
                value = str(value)
            setattr(instance, attr, value)

        instance.modified = now
        instance.modifiedby = user

        update_fields = list(serializer.validated_data.keys()) + ["modified", "modifiedby"]
        # Ensure region is included correctly
        instance.save(using="esmart", update_fields=update_fields)

        return Response(
            SupplierDetailSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Delete supplier",
        tags=["Suppliers"],
        responses={200: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.delete(using="esmart")
        return Response(
            {"message": "Supplier deleted successfully."},
            status=status.HTTP_200_OK,
        )
