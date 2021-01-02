from django.urls import path 

from .views import UserRegisterAPIView, NurseryAdminRegisterAPIView
from dj_rest_auth.views import LogoutView, LoginView, UserDetailsView  

from .views import GoogleLoginAPIView, CheckUserAPIView, CheckUserTypeAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name = 'user_register'),
    path('nursery-admin-register/', NurseryAdminRegisterAPIView.as_view(), name = 'nursery_admin_register'),
    path('login/', LoginView.as_view(), name = 'user_login'),
    path('logout/', LogoutView.as_view(), name = 'user_logout'), 
    path('google-login/', GoogleLoginAPIView.as_view(), name = 'google_login'), 

    path('check-user/', CheckUserAPIView.as_view(), name = 'user_check'), 
    path('user-type/', CheckUserTypeAPIView.as_view(), name = 'user_type_check')
]