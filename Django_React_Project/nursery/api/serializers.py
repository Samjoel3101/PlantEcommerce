from rest_framework import serializers 

from accounts.api.serializers import UserDetailSerializer

from ..models import Nursery, Plant, Order 


class PlantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant 
        fields = ['image', 'name', 'price']


class PlantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant 
        fields = ['id', 'name', 'price', 'image']


class NurseryInlineSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField() 

    class Meta:
        model = Nursery 
        fields = ['name', 'owner']
    
    def get_owner(self, obj):
        owner_data = UserDetailSerializer(obj.admin)
        return owner_data.data


class PlantInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant 
        fields = ['id', 'name', 'price']


class AllPlantsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant 
        fields = ['id', 'image', 'name', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ['plant']


class CartSerializer(serializers.ModelSerializer):
    plant = serializers.SerializerMethodField()

    class Meta:
        model = Order 
        fields = ['plant']

    def get_plant(self, obj):
        plant_data = PlantInlineSerializer(obj.plant)
        return plant_data.data

class UserPlantDetailSerializer(serializers.ModelSerializer):
    nursery = serializers.SerializerMethodField()
    units_ordered = serializers.SerializerMethodField()

    class Meta:
        model = Plant 
        fields = ['id', 'image', 'price', 'name', 'nursery', 'units_ordered']

    def get_nursery(self, obj):
        nursery_data = NurseryInlineSerializer(obj.nursery)
        return nursery_data.data

    def get_units_ordered(self, obj):
        qs = obj.order_set.all()
        request = self.context.get('request')
        if request != None:
            user = request.user 
        else:
            raise ValueError('request is empty')
        qs = qs.filter(user = user)
        return f'{qs.count()}'