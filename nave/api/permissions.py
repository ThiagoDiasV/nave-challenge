from rest_framework import permissions

from .models import Naver


class IsNaverUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow users of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user


class IsProjectNaverOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow users of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        try:
            Naver.objects.get(user=request.user, projects=obj)
            return True
        except Naver.DoesNotExist:
            return False
