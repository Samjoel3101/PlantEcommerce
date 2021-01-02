from rest_framework import serializers 

class PlantQuerySetMixin(object):
    def get_queryset(self, *args, **kwargs):
        if not self.request.user.user_type == 'NUR-ADMIN':
            raise serializers.ValidationError('Permission Denied', 403)
        
        nursery = self.request.user.nursery_set.first() 
        return nursery.plant_set.all()

class NoOrderCheckMixin(object):
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset() 
        
        try:
            length = queryset.count()
        except Exception:
            length =  len(queryset)

        if length == 0:
            return Response({'detail': 'You have made no orders'}, status = 303)
        else:
            return super().get(request, *args, **kwargs)
