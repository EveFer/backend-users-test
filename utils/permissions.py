"""Global Permissions"""
from rest_framework import permissions
import jwt
from django.conf import settings
from utils.validations import (
    ValidationError401,
    ValidationError400
)

class IsAuthenticated(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):

        if 'HTTP_AUTHORIZATION' not in request.META:
            return False
        token = request.META['HTTP_AUTHORIZATION']
        try:
            return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise ValidationError401('Token has expired')
        except jwt.PyJWTError:
            raise ValidationError400('Invalid token')
        return super().has_permission(request, view)



    # def has_object_permission(self, request, view, obj):

    #     token = request.META['HTTP_AUTHORIZATION']
    #     token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    #     return token['user']['id'] == obj.id