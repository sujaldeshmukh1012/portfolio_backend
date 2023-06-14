from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class BlogList(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        # here the views logic is implimented (pending)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class BlogDetail(APIView):
    def get(self, request, slug, format=None):
        blogs = Blog.objects.filter(slug=slug)
        # here the views logic is implimented (pending)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
