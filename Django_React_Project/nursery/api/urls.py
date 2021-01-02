from django.urls import path, include 

from .views import (## Nursery Views
                    PlantCreateAPIView, 
                    PlantListAPIView, 
                    PlantRUDAPIView, 
                    ## User Views
                    AllPlantsListAPIView, 
                    PlaceOrderAPIView, 
                    PlantDetailAPIView, 
                    CartAPIView)

urlpatterns = [
    ## NURSERY API ROUTES
    path('nursery/plant/', include([
        path('create/', PlantCreateAPIView.as_view(), name = 'plant_create_view'),
        path('list/', PlantListAPIView.as_view(), name = 'plant_list_view'),
        path('detail/<int:id>/', PlantRUDAPIView.as_view(), name = 'plant_rud_view')
        ])),

    ## USER API ROUTES 
    path('user/feed/', AllPlantsListAPIView.as_view(), name = 'user_feed'),
    path('user/plant-detail/<int:id>/', PlantDetailAPIView.as_view(), name = 'user_plant_detail'),
    path('user/place-order/', PlaceOrderAPIView.as_view(), name = 'user_place_order'),
    path('user/cart/', CartAPIView.as_view(), name = 'user_cart')
]

