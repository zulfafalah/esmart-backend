from rest_framework import serializers

from legacy.models import Mtsupplier


class SupplierListSerializer(serializers.ModelSerializer[Mtsupplier]):
    class Meta:
        model = Mtsupplier
        fields = [
            "supplierid",
            "suppcode",
            "companyname",
            "address",
            "phone",
            "tempobyr",
            "contactname",
            "islocal",
        ]
        read_only_fields = fields


class SupplierDetailSerializer(serializers.ModelSerializer[Mtsupplier]):
    class Meta:
        model = Mtsupplier
        fields = [
            "supplierid",
            "suppcode",
            "companyname",
            "contactname",
            "contacttitle",
            "address",
            "phone",
            "islocal",
            "region",
            "coa21",
            "tempobyr",
            "email",
            "fax",
            "homepage",
            "currencyid",
            "isactive",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields


class SupplierWriteSerializer(serializers.ModelSerializer[Mtsupplier]):
    region = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Mtsupplier
        fields = [
            "companyname",
            "contacttitle",
            "contactname",
            "address",
            "phone",
            "islocal",
            "region",
            "coa21",
        ]
