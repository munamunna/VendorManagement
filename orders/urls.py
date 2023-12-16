# orders/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchaseOrderViewSet

router = DefaultRouter()
router.register(r'purchase_orders', PurchaseOrderViewSet, basename='purchase-order')
urlpatterns = [
    path('', include(router.urls)),
]


