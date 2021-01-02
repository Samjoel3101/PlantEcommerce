from rest_framework.permissions import BasePermission 

class IsUser(BasePermission):

    def has_permission(self, request, view):
        user = request.user 
        if user.is_authenticated and user.user_type == 'INDIVIDUAL':
            return True 
        else:
            return False