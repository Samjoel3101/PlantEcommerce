from rest_framework import serializers 

class PlantQuerySetMixin(object):
    def get_queryset(self, *args, **kwargs):
        if not self.request.user.user_type == 'NUR-ADMIN':
            raise serializers.ValidationError('Permission Denied', 403)
        
        nursery = self.request.user.nursery_set.first() 
        return nursery.plant_set.all()
