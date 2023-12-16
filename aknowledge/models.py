from django.db import models

# Create your models here.
# aknowledge/models.py

from django.db import models
from orders.models import PurchaseOrder
from performance.models import VendorPerformance
from django.db.models import F, Sum

class Acknowledgment(models.Model):
    purchase_order = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE, related_name='acknowledgment')
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

def recalculate_average_response_time(vendor):
    # Get all acknowledged purchase orders for the vendor
    acknowledged_orders = PurchaseOrder.objects.filter(
        vendor=vendor,
        acknowledgment__acknowledgment_date__isnull=False
    )

    # Calculate total response time
    total_response_time = Sum(F('acknowledgment__acknowledgment_date') - F('issue_date'), output_field=models.DurationField())

    # Calculate the count of acknowledged purchase orders
    total_acknowledged_orders = acknowledged_orders.count()

    # Calculate the average response time
    average_response_time = total_response_time / total_acknowledged_orders if total_acknowledged_orders > 0 else 0

    # Update the average_response_time in the VendorPerformance model
    VendorPerformance.objects.filter(vendor=vendor).update(
        average_response_time=average_response_time
    )

