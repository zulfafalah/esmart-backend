from rest_framework import serializers

from legacy.models import Accounts


class AccountListSerializer(serializers.ModelSerializer[Accounts]):
    akuncode = serializers.CharField(source="code", read_only=True)
    akunname = serializers.CharField(source="name", read_only=True)

    class Meta:
        model = Accounts
        fields = [
            "primarykey",
            "akuncode",
            "akunname",
            "groupkey",
            "parentkey",
            "accounttypekey",
            "limit_saldo_val",
            "isbank",
            "coa0",
            "currac_idf",
        ]
        read_only_fields = fields


class AccountDetailSerializer(serializers.ModelSerializer[Accounts]):
    akuncode = serializers.CharField(source="code", read_only=True)
    akunname = serializers.CharField(source="name", read_only=True)

    class Meta:
        model = Accounts
        fields = [
            "primarykey",
            "akuncode",
            "akunname",
            "groupkey",
            "parentkey",
            "accounttypekey",
            "limit_saldo_val",
            "isbank",
            "coa0",
            "currac_idf",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields


class AccountWriteSerializer(serializers.ModelSerializer[Accounts]):
    akuncode = serializers.CharField(source="code")
    akunname = serializers.CharField(source="name", required=False, allow_blank=True)

    class Meta:
        model = Accounts
        fields = [
            "akuncode",
            "akunname",
            "groupkey",
            "parentkey",
            "accounttypekey",
            "limit_saldo_val",
            "isbank",
            "coa0",
            "currac_idf",
        ]
