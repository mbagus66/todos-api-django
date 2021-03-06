from rest_framework.permissions import BasePermission
from .models import Todos


class IsOwner(BasePermission):
    """Custom permission class to allow todos owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the todos owner."""
        if isinstance(obj, Todos):
            return obj.owner == request.user
        return obj.owner == request.user