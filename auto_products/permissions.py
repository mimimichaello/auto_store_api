from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            if request.method in permissions.SAFE_METHODS:
                return True
        return False

class IsOwnerOfBasket(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
