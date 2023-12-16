from django.shortcuts import render

# orders/views.py
# from rest_framework import viewsets
# from .models import PurchaseOrder
# from .serializers import PurchaseOrderSerializer

# class PurchaseOrderViewSet(viewsets.ModelViewSet):
#     serializer_class = PurchaseOrderSerializer

#     def get_queryset(self):
#         queryset = PurchaseOrder.objects.all()
#         vendor_id = self.request.query_params.get('vendor', None)
#         if vendor_id:
#             queryset = queryset.filter(vendor=vendor_id)
#         return queryset

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

class CreateUpdatePermission(BasePermission):
    """
    Custom permission to allow create and update actions only for authenticated users.
    """
    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS requests (list and retrieve) for all users
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Allow POST and PUT requests (create and update) only for authenticated users
        return request.user.is_authenticated and request.user.user_type == 'customer'

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [CreateUpdatePermission]  # Use custom permission class

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        vendor_id = self.request.query_params.get('vendor', None)
        if vendor_id:
            queryset = queryset.filter(vendor=vendor_id)
        return queryset







