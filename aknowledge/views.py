from django.shortcuts import render

# Create your views here.
from django.db.models import Count, F, Sum
from django.db import transaction
from rest_framework.response import Response
from orders.models import PurchaseOrder
from .serializers import AcknowledgePurchaseOrderSerializer
from .models import recalculate_average_response_time
from rest_framework.decorators import api_view
from rest_framework import status
from django.db import models
from performance.models import VendorPerformance
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import BasePermission


class IsVendorUser(BasePermission):
    """
    Custom permission to allow access only to vendor.
    """
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'vendor'







@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsVendorUser])
def acknowledge_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase Order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = AcknowledgePurchaseOrderSerializer(data=request.data)
       
        if serializer.is_valid():
            acknowledgment_date = serializer.validated_data.get('acknowledgment_date')
            print(acknowledgment_date)
            # Update acknowledgment_date in the PurchaseOrder instance if it's provided
            if acknowledgment_date is not None:
                purchase_order.acknowledgment_date = acknowledgment_date
                purchase_order.save()

                # Recalculate average_response_time for the associated vendor
                recalculate_average_response_time(purchase_order.vendor)

                return Response({'message': 'Purchase Order acknowledged successfully'}, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






