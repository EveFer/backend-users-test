
"""User URLs"""

#django
from django.urls import path, include
#django rest_framework
from rest_framework.routers import DefaultRouter
#views
from users import views as user_views



ROUTER = DefaultRouter()
ROUTER.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(ROUTER.urls)),
]