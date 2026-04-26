from rest_framework import serializers

from legacy.models import Mtcity


class CityListSerializer(serializers.ModelSerializer[Mtcity]):
    class Meta:
        model = Mtcity
        fields = [
            "cityid",
            "cityname",
            "bunitid",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields


class CityDetailSerializer(serializers.ModelSerializer[Mtcity]):
    class Meta:
        model = Mtcity
        fields = [
            "cityid",
            "cityname",
            "bunitid",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields


class CityWriteSerializer(serializers.ModelSerializer[Mtcity]):
    cityname = serializers.CharField(max_length=100)
    bunitid = serializers.IntegerField()

    class Meta:
        model = Mtcity
        fields = [
            "cityname",
            "bunitid",
        ]
