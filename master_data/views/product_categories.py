from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from legacy.models import Mtfamilyprod
from master_data.serializers.product_categories import ProductCategoryDetailSerializer
from master_data.serializers.product_categories import ProductCategoryListSerializer
from master_data.serializers.product_categories import ProductCategoryWriteSerializer


def _generate_famno(last_id: int) -> str:
    """Generate famno in format GRP0001, GRP0002, etc."""
    return f"GRP{last_id:04d}"


class ProductCategoryListCreateView(APIView):
    """
    List all product categories with pagination & search, or create a new one.
    """

    @extend_schema(
        summary="List product categories",
        tags=["Product Categories"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="limit", type=int, description="Items per page (default: 10)"),
            OpenApiParameter(name="search", type=str, description="Search by famno or productfamily"),
        ],
        responses={200: ProductCategoryListSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        limit = max(1, min(100, int(request.query_params.get("limit", 10))))
        search = request.query_params.get("search", "").strip()

        qs = Mtfamilyprod.objects.using("esmart").all().order_by("familyid")

        if search:
            qs = qs.filter(
                Q(famno__icontains=search) | Q(productfamily__icontains=search)
            )

        total = qs.count()
        offset = (page - 1) * limit
        qs = qs[offset : offset + limit]

        serializer = ProductCategoryListSerializer(qs, many=True)
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
        summary="Create product category",
        tags=["Product Categories"],
        request=ProductCategoryWriteSerializer,
        responses={201: ProductCategoryListSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = ProductCategoryWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Determine next famno based on current max familyid
        last = (
            Mtfamilyprod.objects.using("esmart")
            .order_by("-familyid")
            .values_list("familyid", flat=True)
            .first()
        )
        next_id = (last or 0) + 1
        famno = _generate_famno(next_id)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        instance = Mtfamilyprod.objects.using("esmart").create(
            productfamily=serializer.validated_data["productfamily"],
            famno=famno,
            created=now,
            createdby=user,
            modified=now,
            modifiedby=user,
        )

        return Response(
            ProductCategoryListSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class ProductCategoryDetailView(APIView):
    """
    Retrieve, update, or delete a single product category by id.
    """

    def _get_object(self, pk: int) -> Mtfamilyprod:
        try:
            return Mtfamilyprod.objects.using("esmart").get(familyid=pk)
        except Mtfamilyprod.DoesNotExist:
            from rest_framework.exceptions import NotFound

            raise NotFound(detail="Product category not found.")

    @extend_schema(
        summary="Get product category detail",
        tags=["Product Categories"],
        responses={200: ProductCategoryDetailSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = ProductCategoryDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update product category",
        tags=["Product Categories"],
        request=ProductCategoryWriteSerializer,
        responses={200: ProductCategoryListSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = ProductCategoryWriteSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        instance.productfamily = serializer.validated_data["productfamily"]
        instance.modified = now
        instance.modifiedby = user
        instance.save(using="esmart", update_fields=["productfamily", "modified", "modifiedby"])

        return Response(
            ProductCategoryListSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Delete product category",
        tags=["Product Categories"],
        responses={200: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.delete(using="esmart")
        return Response(
            {"message": "Product Category deleted successfully"},
            status=status.HTTP_200_OK,
        )
