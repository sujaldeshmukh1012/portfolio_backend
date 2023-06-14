from rest_framework import serializers
from .models import Services, ServiceEnquiry, ProgrammingTech


class ServiceEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceEnquiry
        fields = "__all__"


class ProgrammingTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingTech
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    tech_stack = ProgrammingTechSerializer(read_only=True, many=True)

    class Meta:
        model = Services
        fields = [
            "name",
            "base_price",
            "tech_stack",
            "description",
            "created_on",
            "poster",
            "slug",
        ]
