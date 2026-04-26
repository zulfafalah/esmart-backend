from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import PermissionDenied
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from legacy.models import Accounts
from legacy.models import Journalentry
from master_data.serializers.accounts import AccountPartialWriteSerializer
from master_data.serializers.accounts import AccountSerializer
from master_data.serializers.accounts import AccountWriteSerializer

ALLOWED_ORDERING_FIELDS = {"primarykey", "code", "name", "groupkey", "accounttypekey", "created", "modified"}


def _is_account_in_journal(primarykey: int) -> bool:
    """Return True if the account is already referenced in journalentry."""
    return Journalentry.objects.using("esmart").filter(accountkey=primarykey).exists()


class AccountListCreateView(APIView):
    """
    GET  /api/v1/master-data/accounts/  — List accounts (paginated, searchable, orderable).
    POST /api/v1/master-data/accounts/  — Create a new account.
    """

    @extend_schema(
        summary="List accounts",
        description="Returns a paginated list of chart-of-accounts entries.",
        tags=["Accounts"],
        parameters=[
            OpenApiParameter(name="page", type=int, description="Page number (default: 1)"),
            OpenApiParameter(name="page_size", type=int, description="Items per page (default: 20)"),
            OpenApiParameter(name="search", type=str, description="Search by code or name"),
            OpenApiParameter(
                name="ordering",
                type=str,
                description="Order results (e.g. code, -code, name). Default: primarykey",
            ),
        ],
        responses={200: AccountSerializer(many=True)},
    )
    def get(self, request: Request) -> Response:
        page = max(1, int(request.query_params.get("page", 1)))
        page_size = max(1, min(100, int(request.query_params.get("page_size", 20))))
        search = request.query_params.get("search", "").strip()
        ordering = request.query_params.get("ordering", "primarykey").strip()

        qs = Accounts.objects.using("esmart").all()

        if search:
            qs = qs.filter(Q(code__icontains=search) | Q(name__icontains=search))

        # Validate ordering to prevent SQL injection
        order_field = ordering.lstrip("-")
        if order_field not in ALLOWED_ORDERING_FIELDS:
            ordering = "primarykey"

        qs = qs.order_by(ordering)

        total = qs.count()
        offset = (page - 1) * page_size
        qs = qs[offset : offset + page_size]

        serializer = AccountSerializer(qs, many=True)

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
        summary="Create account",
        description="Create a new chart-of-accounts entry.",
        tags=["Accounts"],
        request=AccountWriteSerializer,
        responses={201: AccountSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = AccountWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        validated_data = serializer.validated_data
        instance = Accounts.objects.using("esmart").create(
            code=validated_data["code"],
            name=validated_data.get("name", ""),
            groupkey=validated_data["groupkey"],
            parentkey=validated_data.get("parentkey", 0),
            accounttypekey=validated_data["accounttypekey"],
            limit_saldo_val=validated_data.get("limit_saldo_val", 0),
            isbank=validated_data.get("isbank", 0),
            coa0=validated_data.get("coa0", 0),
            currac_idf=validated_data["currac_idf"],
            acpos=0,  # required field in the DB schema with no business default
            created=now,
            createdby=user,
            modified=now,
            modifiedby=user,
        )

        return Response(
            AccountSerializer(instance).data,
            status=status.HTTP_201_CREATED,
        )


class AccountDetailView(APIView):
    """
    GET    /api/v1/master-data/accounts/{primarykey}/  — Retrieve a single account.
    PUT    /api/v1/master-data/accounts/{primarykey}/  — Full update.
    PATCH  /api/v1/master-data/accounts/{primarykey}/  — Partial update.
    DELETE /api/v1/master-data/accounts/{primarykey}/  — Soft-delete (sets coa0=1).
    """

    def _get_object(self, pk: int) -> Accounts:
        try:
            return Accounts.objects.using("esmart").get(primarykey=pk)
        except Accounts.DoesNotExist:
            raise NotFound(detail="Account not found.")

    @extend_schema(
        summary="Get account detail",
        tags=["Accounts"],
        responses={200: AccountSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        serializer = AccountSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Update account (full)",
        description=(
            "Full update (PUT). If the account is already referenced in journalentry, "
            "only limit_saldo_val, isbank, coa0, and currac_idf may be changed."
        ),
        tags=["Accounts"],
        request=AccountWriteSerializer,
        responses={200: AccountSerializer},
    )
    def put(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        in_journal = _is_account_in_journal(pk)

        if in_journal:
            serializer = AccountPartialWriteSerializer(instance, data=request.data)
        else:
            serializer = AccountWriteSerializer(instance, data=request.data)

        serializer.is_valid(raise_exception=True)
        return self._perform_update(request, instance, serializer)

    @extend_schema(
        summary="Update account (partial)",
        description=(
            "Partial update (PATCH). If the account is already referenced in journalentry, "
            "only limit_saldo_val, isbank, coa0, and currac_idf may be changed."
        ),
        tags=["Accounts"],
        request=AccountWriteSerializer,
        responses={200: AccountSerializer},
    )
    def patch(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        in_journal = _is_account_in_journal(pk)

        if in_journal:
            restricted_fields = {"limit_saldo_val", "isbank", "coa0", "currac_idf"}
            sent_fields = set(request.data.keys())
            forbidden = sent_fields - restricted_fields
            if forbidden:
                raise PermissionDenied(
                    detail=(
                        f"Account is already used in journal entries. "
                        f"Only limit_saldo_val, isbank, coa0, currac_idf may be updated. "
                        f"Forbidden fields: {', '.join(sorted(forbidden))}"
                    )
                )
            serializer = AccountPartialWriteSerializer(instance, data=request.data, partial=True)
        else:
            serializer = AccountWriteSerializer(instance, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        return self._perform_update(request, instance, serializer)

    def _perform_update(self, request: Request, instance: Accounts, serializer: AccountWriteSerializer | AccountPartialWriteSerializer) -> Response:  # type: ignore[type-arg]
        now = timezone.now()
        user = request.user.get_username() if request.user.is_authenticated else "system"

        for attr, value in serializer.validated_data.items():
            setattr(instance, attr, value)

        instance.modified = now
        instance.modifiedby = user

        update_fields = list(serializer.validated_data.keys()) + ["modified", "modifiedby"]
        instance.save(using="esmart", update_fields=update_fields)

        return Response(
            AccountSerializer(instance).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Deactivate account (soft-delete)",
        description="Sets coa0=1 (Non Aktif) instead of permanently deleting the record.",
        tags=["Accounts"],
        responses={204: None},
    )
    def delete(self, request: Request, pk: int) -> Response:
        instance = self._get_object(pk)
        instance.coa0 = 1
        instance.modified = timezone.now()
        instance.modifiedby = request.user.get_username() if request.user.is_authenticated else "system"
        instance.save(using="esmart", update_fields=["coa0", "modified", "modifiedby"])
        return Response(status=status.HTTP_204_NO_CONTENT)
