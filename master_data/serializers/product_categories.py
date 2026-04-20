from rest_framework import serializers

from legacy.models import Mtfamilyprod


class ProductCategoryListSerializer(serializers.ModelSerializer[Mtfamilyprod]):
    """Serializer for list response — minimal fields."""

    class Meta:
        model = Mtfamilyprod
        fields = ["familyid", "famno", "productfamily"]
        read_only_fields = ["familyid", "famno", "productfamily"]


class ProductCategoryDetailSerializer(serializers.ModelSerializer[Mtfamilyprod]):
    """Serializer for detail response — full fields."""

    class Meta:
        model = Mtfamilyprod
        fields = [
            "familyid",
            "famno",
            "productfamily",
            "bunitid",
            "coa15",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]
        read_only_fields = [
            "familyid",
            "famno",
            "created",
            "createdby",
            "modified",
            "modifiedby",
        ]


class ProductCategoryWriteSerializer(serializers.ModelSerializer[Mtfamilyprod]):
    """Serializer for create / update — only writable user-supplied fields."""

    class Meta:
        model = Mtfamilyprod
        fields = ["productfamily"]
