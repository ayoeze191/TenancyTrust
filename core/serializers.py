# core/serializers.py
from rest_framework import serializers
from .models import Property, TenantProfile, Agreement, Picture
class TenantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantProfile
        fields = '__all__'

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'


class PropertyImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image', read_only=True)

    class Meta:
        model = Picture
        fields = ['id', 'image_url']

class PropertySerializer(serializers.ModelSerializer):
    pictures = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'