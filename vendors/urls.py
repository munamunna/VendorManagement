# orders/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorsViewSet

router = DefaultRouter()
router.register('vendors', VendorsViewSet, basename='vendors')
urlpatterns = [
    path('', include(router.urls)),
]


