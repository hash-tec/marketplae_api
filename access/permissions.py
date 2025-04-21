from rest_framework.permissions import BasePermission


class AuthorEditAddressOnly(BasePermission):
    edit_method = ['POST', 'PUT', 'PATCH', 'DELETE']
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.user == obj.customer:
            return True
        elif request.user.is_staff and request.method in self.edit_method:
            return False