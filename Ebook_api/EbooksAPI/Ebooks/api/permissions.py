from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        print("is_admin",is_admin)
        return request.method in permissions.SAFE_METHODS or is_admin