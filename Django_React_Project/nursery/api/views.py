from rest_framework import serializers 
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions 
from rest_framework.parsers import MultiPartParser, FormParser 


from .serializers import (PlantCreateSerializer, 
                         PlantDetailSerializer, 
                         AllPlantsDetailSerializer,
                         OrderSerializer, 
                         CartSerializer, 
                         UserPlantDetailSerializer, 
                         NurseryPlantOrderSerializer)
                         
from .mixins import PlantQuerySetMixin, NoOrderCheckMixin
from ..models import Nursery, Plant, Order
from .permissions import IsUser, IsNurseryAdmin 


################  NURSERY VIEWS ###################

class PlantCreateAPIView(CreateAPIView):
    serializer_class = PlantCreateSerializer 
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        if not self.request.user.user_type == 'NUR-ADMIN':
            return Response(data = {'detail': 'Permission Denied'}, status = 403)
        nursery = self.request.user.nursery_set.first()
        instance = serializer.save(nursery = nursery)


class PlantListAPIView(PlantQuerySetMixin, ListAPIView):
    serializer_class = PlantDetailSerializer 

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.count() == 0:
            return Response({'detail': 'No plants'}, status = 303)
        else:
            return super().get(request, *args, **kwargs)


class PlantRUDAPIView(PlantQuerySetMixin, RetrieveUpdateDestroyAPIView):
    serializer_class =  PlantDetailSerializer
    
    def get_object(self, *args, **kwargs):
        id = self.kwargs.get('id')
        queryset = self.get_queryset(*args, **kwargs)
        qs_ids = [q.id for q in queryset]
        
        if id not in qs_ids:
            raise serializers.ValidationError('Invalid id', 404)
        obj = queryset.filter(id = id)
        return obj.first()  

class ViewOrdersAPIView(NoOrderCheckMixin, ListAPIView):
    serializer_class = NurseryPlantOrderSerializer 
    permission_classes = [IsNurseryAdmin]

    def get_queryset(self, *args, **kwargs):
        nursery = self.request.user.nursery_set.first()
        qs = Order.objects.filter(plant__nursery = nursery)
        if qs.count() == 0:
            return qs 
        else:
            unique_plant_ids = self._get_unique_ids(qs)
            qs = [Plant.objects.get(id = id) for id in unique_plant_ids]
            return qs

    def _get_unique_ids(self, qs):
        qs_ids = [q.plant.id for q in qs]
        unique_ids = []
        for id in qs_ids:
            if id not in unique_ids:
                unique_ids.append(id)
        return unique_ids 

######################## USER VIEWS #########################

class AllPlantsListAPIView(ListAPIView):
    serializer_class = AllPlantsDetailSerializer 
    queryset = Plant.objects.all()
    permission_classes = [IsUser] 


class PlaceOrderAPIView(CreateAPIView):
    serializer_class = OrderSerializer 
    permission_classes = [IsUser]

    def perform_create(self, serializer):
        instance = serializer.save(user= self.request.user)


class PlantDetailAPIView(RetrieveAPIView):
    serializer_class = UserPlantDetailSerializer 
    permission_classes = [IsUser] 

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request} 
        
    def get_queryset(self, *args, **kwargs):
        return Plant.objects.all() 

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get('id')
        queryset = self.get_queryset(*args, **kwargs)
        return queryset.filter(id = id).first()


class CartAPIView(NoOrderCheckMixin, ListAPIView):
    serializer_class = CartSerializer 
    permission_classes = [IsUser]

    def get_queryset(self, *args, **kwargs):
        queryset = Order.objects.filter(user = self.request.user)
        return queryset