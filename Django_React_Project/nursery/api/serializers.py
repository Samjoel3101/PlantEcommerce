from rest_framework import serializers 

from ..models import Nursery, Plant 

class PlantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant 
        fields = ['image', 'name', 'price']

class PlantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant 
        fields = ['id', 'name', 'price', 'image']