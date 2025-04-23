from rest_framework.permissions import BasePermission
class UserPermission(BasePermission):
    edit_method = ['POST', 'PUT', 'PATCH', 'DELETE']
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.user == obj.seller:
            return True
        elif request.user.is_staff and request.method in self.edit_method:
            return False
        return False

class AuthorEditOnly(BasePermission):
    edit_method = ['POST', 'PUT', 'PATCH', 'DELETE']
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.user == obj.customer:
            return True
        elif request.user.is_staff and request.method in self.edit_method:
            return False
        return False


class CartPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.user != obj.owner:
            return False
        return True

class ReviewPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        elif not request.user.is_authenticated and request.method == 'GET':
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user != obj.owner:
            return False
        return True


