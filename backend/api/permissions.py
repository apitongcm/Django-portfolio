from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    """"
        Create permissions to only Carl can edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner
        return obj.author == request.user