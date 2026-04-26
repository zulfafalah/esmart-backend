from rest_framework import serializers

from legacy.models import Accounts
from legacy.models import Mtcurrency
from legacy.models import Mtgrupcoa

ACCOUNT_TYPE_MAP = {0: "DETIL", 1: "GRUP"}


class AccountSerializer(serializers.ModelSerializer[Accounts]):
    """
    Read serializer — includes computed/joined display fields.
    Used for list, detail, and all write-response bodies.
    """

    groupname = serializers.SerializerMethodField()
    parentname = serializers.SerializerMethodField()
    accounttype = serializers.SerializerMethodField()
    currencyname = serializers.SerializerMethodField()

    class Meta:
        model = Accounts
        fields = [
            "primarykey",
            "code",
            "name",
            "groupkey",
            "groupname",
            "parentkey",
            "parentname",
            "accounttypekey",
            "accounttype",
            "limit_saldo_val",
            "isbank",
            "coa0",
            "currac_idf",
            "currencyname",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields

    def get_groupname(self, obj: Accounts) -> str | None:
        if not obj.groupkey:
            return None
        try:
            group = Mtgrupcoa.objects.using("esmart").get(primarykey=obj.groupkey)
            return group.groupname
        except Mtgrupcoa.DoesNotExist:
            return None

    def get_parentname(self, obj: Accounts) -> str | None:
        if not obj.parentkey:
            return None
        try:
            parent = Accounts.objects.using("esmart").get(primarykey=obj.parentkey)
            return parent.name
        except Accounts.DoesNotExist:
            return None

    def get_accounttype(self, obj: Accounts) -> str | None:
        return ACCOUNT_TYPE_MAP.get(obj.accounttypekey)  # type: ignore[arg-type]

    def get_currencyname(self, obj: Accounts) -> str | None:
        if not obj.currac_idf:
            return None
        try:
            currency = Mtcurrency.objects.using("esmart").get(currency_pk=obj.currac_idf)
            return currency.currencyname
        except Mtcurrency.DoesNotExist:
            return None


class AccountWriteSerializer(serializers.ModelSerializer[Accounts]):
    """
    Write serializer — validates input for create / update.
    """

    class Meta:
        model = Accounts
        fields = [
            "code",
            "name",
            "groupkey",
            "parentkey",
            "accounttypekey",
            "limit_saldo_val",
            "isbank",
            "coa0",
            "currac_idf",
        ]

    def validate_currac_idf(self, value: int) -> int:
        if not value:
            raise serializers.ValidationError("currac_idf is required and cannot be 0.")
        return value

    def validate_groupkey(self, value: int) -> int:
        if not value:
            raise serializers.ValidationError("groupkey is required and cannot be 0.")
        return value


class AccountPartialWriteSerializer(serializers.ModelSerializer[Accounts]):
    """
    Partial write serializer — only allows fields that may always be updated
    (used when the account is already referenced in journalentry).
    """

    class Meta:
        model = Accounts
        fields = [
            "limit_saldo_val",
            "isbank",
            "coa0",
            "currac_idf",
        ]
