from rest_framework import serializers

from legacy.models import Mtuser


class SalesListSerializer(serializers.ModelSerializer[Mtuser]):
    class Meta:
        model = Mtuser
        fields = [
            "userid",
            "usercode",
            "username",
            "utelp1",
            "email",
            "issales",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields


class SalesDetailSerializer(serializers.ModelSerializer[Mtuser]):
    class Meta:
        model = Mtuser
        fields = [
            "userid",
            "usercode",
            "username",
            "utelp1",
            "email",
            "issales",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields


class SalesWriteSerializer(serializers.ModelSerializer[Mtuser]):
    usercode = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=100)
    utelp1 = serializers.CharField(max_length=30, required=False, allow_blank=True)
    email = serializers.CharField(max_length=100, required=False, allow_blank=True)
    issales = serializers.IntegerField()

    class Meta:
        model = Mtuser
        fields = [
            "usercode",
            "username",
            "utelp1",
            "email",
            "issales",
        ]
