from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from legacy.models import Accounts
from master_data.serializers.accounts import AccountDetailSerializer
from master_data.serializers.accounts import AccountListSerializer
from master_data.serializers.accounts import AccountWriteSerializer


class AccountListCreateView(APIView):
    """
    List all accounts with pagination & search, or create a new one.
    """

    @extend_schema(
        summary="List accounts",
        tags=["Accounts"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="limit", type=int, description="Items per page (default: 10)"),
            OpenApiParameter(name="search", type=str, description="Search by code or name"),
        ],
        responses={200: AccountListSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        limit = max(1, min(100, int(request.query_params.get("limit", 10))))
        search = request.query_params.get("search", "").strip()

        qs = Accounts.objects.using("esmart").all().order_by("primarykey")

        if search:
            qs = qs.filter(
                Q(code__icontains=search) | Q(name__icontains=search)
            )

        total = qs.count()
        offset = (page - 1) * limit
        qs = qs[offset : offset + limit]

        serializer = AccountListSerializer(qs, many=True)
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
        summary="Create account",
        tags=["Accounts"],
        request=AccountWriteSerializer,
        responses={201: AccountListSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = AccountWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        
        # `acpos` is a required field without a default in the model, defaulting to 0
        validated_data["acpos"] = 0
        validated_data["created"] = now
        validated_data["createdby"] = user
        validated_data["modified"] = now
        validated_data["modifiedby"] = user

        instance = Accounts.objects.using("esmart").create(**validated_data)

        return Response(
            AccountListSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class AccountDetailView(APIView):
    """
    Retrieve, update, or delete a single account by id.
    """

    def _get_object(self, pk: int) -> Accounts:
        try:
            return Accounts.objects.using("esmart").get(primarykey=pk)
        except Accounts.DoesNotExist:
            from rest_framework.exceptions import NotFound

            raise NotFound(detail="Account not found.")

    @extend_schema(
        summary="Get account detail",
        tags=["Accounts"],
        responses={200: AccountDetailSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = AccountDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update account",
        tags=["Accounts"],
        request=AccountWriteSerializer,
        responses={200: AccountListSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = AccountWriteSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        for attr, value in serializer.validated_data.items():
            setattr(instance, attr, value)
            
        instance.modified = now
        instance.modifiedby = user
        
        # Determine updated fields plus modified fields
        update_fields = list(serializer.validated_data.keys()) + ["modified", "modifiedby"]
        instance.save(using="esmart", update_fields=update_fields)

        return Response(
            AccountListSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Delete account",
        tags=["Accounts"],
        responses={200: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.delete(using="esmart")
        return Response(
            {"message": "Account deleted successfully"},
            status=status.HTTP_200_OK,
        )
