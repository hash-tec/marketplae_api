from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS
from rest_framework.response import Response

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if  request.method in SAFE_METHODS or request.user.is_authenticated:
            return False
    def has_object_permission(self, request, view, obj):
        if request.user == obj.seller:
            return True
        return super().has_object_permission(request, view, obj)
    

 