from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Services, ServiceEnquiry, ProgrammingTech
from .serializers import (
    ServiceEnquirySerializer,
    ProgrammingTechSerializer,
    ServiceSerializer,
)


class ServiceList(APIView):
    def get(self, request, format=None):
        services = Services.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class ProgrammingList(APIView):
    def get(self, request, format=None):
        tech = ProgrammingTech.objects.all()
        serializer = ProgrammingTechSerializer(tech, many=True)
        return Response(serializer.data)


class ServiceEnquiryView(APIView):
    def get(self, request, format=None):
        s_e = ServiceEnquiry.objects.all()
        serializer = ServiceEnquirySerializer(s_e, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
