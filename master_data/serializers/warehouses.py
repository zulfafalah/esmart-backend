from rest_framework import serializers

from legacy.models import Mtwhs


class WarehouseListSerializer(serializers.ModelSerializer[Mtwhs]):
    class Meta:
        model = Mtwhs
        fields = [
            "whsid",
            "whscode",
            "whsname",
            "whsloc",
            "whstelp",
            "whsman",
        ]
        read_only_fields = fields


class WarehouseDetailSerializer(serializers.ModelSerializer[Mtwhs]):
    class Meta:
        model = Mtwhs
        fields = [
            "whsid",
            "whscode",
            "whsname",
            "whsloc",
            "whstelp",
            "whsman",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields


class WarehouseWriteSerializer(serializers.ModelSerializer[Mtwhs]):
    class Meta:
        model = Mtwhs
        fields = [
            "whscode",
            "whsname",
            "whsloc",
            "whstelp",
            "whsman",
        ]
