from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from legacy.models import Mtuser
from master_data.serializers.sales import SalesDetailSerializer
from master_data.serializers.sales import SalesListSerializer
from master_data.serializers.sales import SalesWriteSerializer


class SalesListCreateView(APIView):
    """
    List all sales representatives with pagination & search, or create a new one.
    Sales reps are stored in `mtuser` where `issales = 1`.
    """

    @extend_schema(
        summary="List sales",
        tags=["Sales"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="page_size", type=int, description="Items per page (default: 20)"),
            OpenApiParameter(name="search", type=str, description="Search by user code or name"),
            OpenApiParameter(
                name="ordering",
                type=str,
                description="Order results (e.g. usercode, -usercode, username)",
            ),
        ],
        responses={200: SalesListSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        page_size = max(1, min(100, int(request.query_params.get("page_size", 20))))
        search = request.query_params.get("search", "").strip()
        ordering = request.query_params.get("ordering", "userid").strip()

        # Sales reps: issales = 1
        qs = Mtuser.objects.using("esmart").filter(issales=1)

        if search:
            qs = qs.filter(Q(usercode__icontains=search) | Q(username__icontains=search))

        # Validate ordering field to prevent injection
        allowed_ordering_fields = {"userid", "usercode", "username", "created", "modified"}
        order_field = ordering.lstrip("-")
        if order_field not in allowed_ordering_fields:
            ordering = "userid"

        qs = qs.order_by(ordering)

        total = qs.count()
        offset = (page - 1) * page_size
        qs = qs[offset : offset + page_size]

        serializer = SalesListSerializer(qs, many=True)

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
        summary="Create sales",
        tags=["Sales"],
        request=SalesWriteSerializer,
        responses={201: SalesDetailSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = SalesWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        instance = Mtuser.objects.using("esmart").create(
            usercode=validated_data["usercode"],
            username=validated_data["username"],
            utelp1=validated_data.get("utelp1", ""),
            email=validated_data.get("email", ""),
            issales=validated_data["issales"],
            # System defaults for required fields
            deptid=0,
            upperlevelid=0,
            password="",
            levelsecurity=0,
            email2="",
            signatureid="",
            photoid="",
            creditlimit=0,
            created=now,
            createdby=user,
            modified=now,
            modifiedby=user,
        )

        return Response(
            SalesDetailSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class SalesDetailView(APIView):
    """
    Retrieve, update, or delete a single sales representative by userid.
    Ensures the record is a sales rep (issales = 1).
    """

    def _get_object(self, pk: int) -> Mtuser:
        try:
            return Mtuser.objects.using("esmart").filter(issales=1).get(userid=pk)
        except Mtuser.DoesNotExist:
            raise NotFound(detail="Sales not found.")

    @extend_schema(
        summary="Get sales detail",
        tags=["Sales"],
        responses={200: SalesDetailSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = SalesDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update sales (full)",
        tags=["Sales"],
        request=SalesWriteSerializer,
        responses={200: SalesDetailSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = SalesWriteSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        instance.usercode = validated_data["usercode"]
        instance.username = validated_data["username"]
        instance.utelp1 = validated_data.get("utelp1", instance.utelp1)
        instance.email = validated_data.get("email", instance.email)
        instance.issales = validated_data["issales"]
        instance.modified = now
        instance.modifiedby = user

        instance.save(
            using="esmart",
            update_fields=["usercode", "username", "utelp1", "email", "issales", "modified", "modifiedby"],
        )

        return Response(
            SalesDetailSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Partial update sales",
        tags=["Sales"],
        request=SalesWriteSerializer,
        responses={200: SalesDetailSerializer},
    )
    def patch(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = SalesWriteSerializer(instance, data=request.data, partial=True)
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
            SalesDetailSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Delete sales",
        tags=["Sales"],
        responses={204: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.delete(using="esmart")
        return Response(status=status.HTTP_204_NO_CONTENT)
