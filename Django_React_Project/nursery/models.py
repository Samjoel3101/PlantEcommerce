from django.db import models

from accounts.models import NurseryAdmin, Individual

### NURSERY MODELS 
class Nursery(models.Model):
    name = models.CharField(max_length = 64, null = True, blank = True)
    location = models.CharField(max_length = 256, null = True, blank = True)
    admin = models.ForeignKey(NurseryAdmin, on_delete = models.CASCADE, default = 1)


class Plant(models.Model):
    image = models.ImageField(upload_to = 'media', null = True, blank = True)
    name = models.CharField(max_length = 64)
    price = models.IntegerField()
    nursery = models.ForeignKey(Nursery, on_delete = models.CASCADE)


### USER MODELS 
class Order(models.Model):
    plant = models.ForeignKey(Plant, on_delete = models.CASCADE)
    user  = models.ForeignKey(Individual, on_delete = models.CASCADE)
