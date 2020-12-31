from django.db import models
from django.db.models.signals import pre_save, post_save 
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):

    class UserTypes(models.TextChoices):
        Individual = "INDIVIDUAL", "INDIVIDUAL"
        NurseryAdmin  = "NUR-ADMIN", "NUR-ADMIN"
    
    user_type = models.CharField(max_length = 25, default = UserTypes.Individual)

class IndividualManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type = User.UserTypes.Individual)

class Individual(User):
    objects = IndividualManager()

    class Meta:
        proxy = True 

class NurseryAdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type = User.UserTypes.NurseryAdmin)

class NurseryAdmin(User):
    objects = NurseryAdminManager()

    class Meta:
        proxy = True 
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = 'NUR-ADMIN'
        return super().save(*args, **kwargs)

def create_nursery(sender, instance, *args, **kwargs):
    instance.nursery_set.create() 

post_save.connect(create_nursery, sender = NurseryAdmin)

