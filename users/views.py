"""Instructor Views"""

# from django.shortcuts import get_object_or_404
# django rest framework
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
# Permissions
from rest_framework.permissions import AllowAny
# Serializers
from users.serializers import (
    UserModelSerializer,
    UserResponseModelSerializer,
    UserLoginSerializer,
)
# Models
from users.models import User
# Permissions
from utils.permissions import IsAuthenticated

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """User viewSet"""

    queryset = User.objects.all()
    # serializer_class = InstructorModelSerializer
    # serializer_output_class = InstructorResponseModelSerializer
    lookup_field = 'id'

    def get_permissions(self):
        """Assing permissions baseIsAuthenticatedd on action"""
        if self.action in ['create', 'login']:
            permissions = [AllowAny]
        elif  self.action in ['update', 'partial_update', 'retrieve', 'List']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_serializer_class(self): #obtener el serializer de acuerdo en acciones
        """Return serializer based on action"""
        if self.action in ['create', 'update', 'partial_update']:
            return UserModelSerializer
        if self.action in ['retrieve', 'list']:
            return UserResponseModelSerializer
        return UserResponseModelSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        """Instructor Login"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
