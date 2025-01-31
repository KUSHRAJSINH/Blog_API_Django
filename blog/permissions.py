from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of an object (post or comment) 
    to edit or delete it. Others can only read.
    """
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow editing/deleting only if the user is the author (for posts) or user (for comments)
        if hasattr(obj, 'author'):  # If object has 'author' (Post model)
            return obj.author == request.user
        elif hasattr(obj, 'user'):  # If object has 'user' (Comment model)
            return obj.user == request.user

        return False  # Deny permission if neither condition is met
