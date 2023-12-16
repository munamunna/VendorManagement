from django.shortcuts import render

# performance/views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import VendorPerformance
from .seriallizers import VendorPerformanceMetricsSerializer
from orders.models import PurchaseOrder
from django.db.models import Count, Avg
from django.utils import timezone
from django.db.models import F, ExpressionWrapper, fields
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class VendorPerformanceMetricsView(generics.RetrieveAPIView):
    serializer_class = VendorPerformanceMetricsSerializer
    authentication_classes = [TokenAuthentication]  # Add token authentication
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        vendor_id = self.kwargs['vendor_id']
        return VendorPerformance.objects.filter(vendor_id=vendor_id)

    def get(self, request, *args, **kwargs):
        vendor_id = self.kwargs['vendor_id']

        # Calculate performance metrics based on the provided logic
        on_time_delivery_rate = self.calculate_on_time_delivery_rate(vendor_id)
        quality_rating_avg = self.calculate_quality_rating_avg(vendor_id)
        average_response_time = self.calculate_average_response_time(vendor_id)
        fulfillment_rate = self.calculate_fulfillment_rate(vendor_id)

        # Prepare the response data
        response_data = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate,
        }

        return Response(response_data)

    def calculate_on_time_delivery_rate(self, vendor_id):
        completed_pos = PurchaseOrder.objects.filter(
            vendor_id=vendor_id,
            status='completed',
            delivery_date__lte=timezone.now()
        ).count()

        total_completed_pos = PurchaseOrder.objects.filter(
            vendor_id=vendor_id,
            status='completed'
        ).count()

        if total_completed_pos == 0:
            return 0.0

        return completed_pos / total_completed_pos * 100.0

    def calculate_quality_rating_avg(self, vendor_id):
        return PurchaseOrder.objects.filter(
            vendor_id=vendor_id,
            status='completed',
            quality_rating__isnull=False
        ).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0

    def calculate_average_response_time(self, vendor_id):
        response_times = PurchaseOrder.objects.filter(
            vendor_id=vendor_id,
            acknowledgment_date__isnull=False
        ).annotate(
            response_time=ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=fields.DurationField()
            )
        ).aggregate(Avg('response_time'))

        return response_times.get('response_time__avg') or 0.0
      

    def calculate_fulfillment_rate(self, vendor_id):
        successful_pos = PurchaseOrder.objects.filter(
            vendor_id=vendor_id,
            status='completed',
            issue_date__isnull=True
        ).count()

        total_pos = PurchaseOrder.objects.filter(
            vendor_id=vendor_id,
            status='completed'
        ).count()

        if total_pos == 0:
            return 0.0

        return successful_pos / total_pos * 100.0

