from django.urls import path, include 

from .views import PlantCreateAPIView, PlantListAPIView, PlantRUDAPIView

urlpatterns = [
    path('plant/', include([
        path('create/', PlantCreateAPIView.as_view(), name = 'plant_create_view'),
        path('list/', PlantListAPIView.as_view(), name = 'plant_list_view'),
        path('detail/<int:id>/', PlantRUDAPIView.as_view(), name = 'plant_rud_view')
        ])),
]

