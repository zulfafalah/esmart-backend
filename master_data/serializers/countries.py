from rest_framework import serializers

from legacy.models import Mtcity


class CountryListSerializer(serializers.ModelSerializer[Mtcity]):
    class Meta:
        model = Mtcity
        fields = [
            "cityid",
            "cityname",
        ]
        read_only_fields = fields


class CountryDetailSerializer(serializers.ModelSerializer[Mtcity]):
    class Meta:
        model = Mtcity
        fields = [
            "cityid",
            "cityname",
            "citycountry",
            "coa10",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields


class CountryWriteSerializer(serializers.ModelSerializer[Mtcity]):
    class Meta:
        model = Mtcity
        fields = [
            "cityname",
        ]
