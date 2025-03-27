from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS, IsAdminUser
from rest_framework.response import Response
class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    

    def has_object_permission(self, request, view, obj):
        return request.user == obj.seller
    




# class CartPermission