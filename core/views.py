from django.shortcuts import render

# Create your views here.
# core/views.py
from rest_framework import viewsets
from .models import Property, TenantProfile, Agreement, Picture
from .serializers import PropertySerializer, TenantProfileSerializer, AgreementSerializer, PropertyImageSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class TenantProfileViewSet(viewsets.ModelViewSet):
    queryset = TenantProfile.objects.all()
    serializer_class = TenantProfileSerializer

class AgreementViewSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer



class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PropertyImageSerializer