from django.urls import path, include 

urlpatterns = [
    path('accounts/', include('accounts.api.urls')), 
    path('nursery/', include('nursery.api.urls'))
]