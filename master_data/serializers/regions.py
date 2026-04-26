from rest_framework import serializers

from legacy.models import Mtcity
from legacy.models import Mtregion


class RegionListSerializer(serializers.ModelSerializer[Mtregion]):
    cityname = serializers.SerializerMethodField()

    class Meta:
        model = Mtregion
        fields = [
            "regionid",
            "cityid",
            "cityname",
            "regioncode",
            "regionname",
            "coa19",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields

    def get_cityname(self, obj: Mtregion) -> str:
        try:
            city = Mtcity.objects.using("esmart").get(cityid=obj.cityid)
            return city.cityname
        except Mtcity.DoesNotExist:
            return ""


class RegionDetailSerializer(serializers.ModelSerializer[Mtregion]):
    cityname = serializers.SerializerMethodField()

    class Meta:
        model = Mtregion
        fields = [
            "regionid",
            "cityid",
            "cityname",
            "regioncode",
            "regionname",
            "coa19",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = fields

    def get_cityname(self, obj: Mtregion) -> str:
        try:
            city = Mtcity.objects.using("esmart").get(cityid=obj.cityid)
            return city.cityname
        except Mtcity.DoesNotExist:
            return ""


class RegionWriteSerializer(serializers.ModelSerializer[Mtregion]):
    cityid = serializers.IntegerField()
    regioncode = serializers.CharField(max_length=50)
    regionname = serializers.CharField(max_length=100)

    class Meta:
        model = Mtregion
        fields = [
            "cityid",
            "regioncode",
            "regionname",
        ]
