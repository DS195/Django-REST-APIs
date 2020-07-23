from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        print("is_admin",is_admin)
        return request.method in permissions.SAFE_METHODS or is_admin

class IsReviewAuthorOrReadonly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.review_author == request.user
