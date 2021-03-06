from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser, User


class IsStaff(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return request.user and request.user.is_staff

        # Write permissions are only allowed to the owner of the snippet.
        return request.user and request.user.is_staff