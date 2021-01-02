from django.contrib.auth import get_user_model

from rest_framework import serializers 
from rest_framework.serializers import Serializer  
from rest_framework.authtoken.models import Token 

from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer

from ..models import User 
from ..adapter import UserTypeDefaultAdapter, NurseryAdminAdapter

class CheckUserSerializer(Serializer): 

    token = serializers.CharField(max_length = 120)  

    def validate(self, data):
        token = data.get('token') 
        
        token_obj = Token.objects.filter(key = token)

        if token_obj.count() == 0:
            raise serializers.ValidationError('Such a user does not exist') 
        elif token_obj.count() > 1:
            raise serializers.ValidationError('More than one user exist with this token which is not possible. Malicious Activity found')
        else:   
            data['token_obj'] = token_obj[0]     
            return data 

class UserRegisterSerializer(RegisterSerializer):
    adapter = UserTypeDefaultAdapter 

    def save(self, request):
        adapter = self.adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

class NurseryAdminRegisterSerializer(UserRegisterSerializer):
    adapter = NurseryAdminAdapter
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username']