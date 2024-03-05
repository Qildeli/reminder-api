from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Permission class to check if user is an owner of the task.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner and obj.owner == request.user
