from rest_framework import permissions

class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj == request.user:
            allowed_fields = ['first_name', 'last_name', 'image']
            data_fields = request.data.keys()
            for field in data_fields:
                if field not in allowed_fields:
                    return False
            return True
        return False
