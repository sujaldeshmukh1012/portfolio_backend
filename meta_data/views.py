from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WebVisits, NewsLetter
from .serializers import WebVisitsSerializer, NewsLetterSerializer


class WebVisitsView(APIView):
    def get(self, request, format=None):
        s_e = WebVisits.objects.all()
        serializer = WebVisitsSerializer(s_e, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WebVisitsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsLetterView(APIView):
    def get(self, request, format=None):
        s_e = NewsLetter.objects.all()
        serializer = NewsLetterSerializer(s_e, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewsLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
