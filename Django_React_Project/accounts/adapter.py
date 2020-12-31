from allauth.account.adapter import DefaultAccountAdapter 
from .models import Individual, NurseryAdmin

class UserTypeDefaultAdapter(DefaultAccountAdapter):
    user_model = Individual 

    def new_user(self, request):
        user = self.user_model() 
        return user 

class NurseryAdminAdapter(UserTypeDefaultAdapter):
    user_model = NurseryAdmin

