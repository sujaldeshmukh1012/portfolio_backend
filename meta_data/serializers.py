from rest_framework import serializers
from .models import WebVisits, NewsLetter


class WebVisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebVisits
        fields = "__all__"


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = "__all__"
