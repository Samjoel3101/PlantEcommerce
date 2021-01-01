from rest_framework import serializers 
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions 
from rest_framework.parsers import MultiPartParser, FormParser 

from .serializers import PlantCreateSerializer, PlantDetailSerializer 
from .mixins import PlantQuerySetMixin 


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
