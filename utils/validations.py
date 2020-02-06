
"""Costum validation"""
from rest_framework.exceptions import APIException
from rest_framework import status

class ValidationError400(APIException):
    """Status code"""
    status_code = status.HTTP_400_BAD_REQUEST

class ValidationError401(APIException):
    """Status code"""
    status_code = status.HTTP_401_UNAUTHORIZED

class ValidationError403(APIException):
    """Status code"""
    status_code = status.HTTP_403_FORBIDDEN