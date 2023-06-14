from rest_framework import serializers
from .models import *


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogViews
        fields = "__all__"


class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLike
        fields = "__all__"


class ExternalLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalLinks
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        tags = TagsSerializer(
            many=True,
        )

    category = CategorySerializer(
        many=True,
    )
    views = BlogViewsSerializer(
        many=True,
    )
    likes = BlogLikeSerializer(
        many=True,
    )
    external_links = ExternalLinksSerializer(many=True)
