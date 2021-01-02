from rest_framework.permissions import BasePermission 

class CheckUserType(BasePermission):
    user_type = 'INDIVIDUAL'
    def has_permission(self, request, view):
        user = request.user 
        if user.is_authenticated and user.user_type == self.user_type:
            return True 
        else:
            return False

class IsUser(CheckUserType):
    pass 
    
class IsNurseryAdmin(BasePermission):
    user_type = 'NUR-ADMIN'