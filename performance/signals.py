from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import PurchaseOrder
from performance.models import VendorPerformance
from django.db import models
from django.db import transaction
from django.db.models import F, Sum
from django.utils import timezone

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_on_po_save(sender, instance, **kwargs):
    if instance.status == 'completed':
        # Update VendorPerformance metrics when a purchase order is completed
        recalculate_metrics_on_po_completion(instance.vendor)

@transaction.atomic
def recalculate_metrics_on_po_completion(vendor):
    # Get all completed purchase orders for the vendor
    completed_orders = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed',
        delivery_date__lte=timezone.now()
    )

    # Calculate on-time delivery rate
    on_time_delivery_rate = calculate_on_time_delivery_rate(completed_orders)

    # Calculate quality rating average
    quality_rating_avg = calculate_quality_rating_average(completed_orders)

    # Update metrics in the VendorPerformance model
    VendorPerformance.objects.filter(vendor=vendor).update(
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg
    )

def calculate_on_time_delivery_rate(completed_orders):
    total_completed_orders = completed_orders.count()
    
    if total_completed_orders == 0:
        return 0  # No completed orders, on-time delivery rate is 0
    
    on_time_delivery_count = completed_orders.filter(
        delivery_date__lte=F('acknowledgment_date')
    ).count()

    on_time_delivery_rate = (on_time_delivery_count / total_completed_orders) * 100.0
    return round(on_time_delivery_rate, 2)


def calculate_quality_rating_average(completed_orders):

    total_completed_orders = completed_orders.count()

    if total_completed_orders == 0:
        return None  # No completed orders, quality rating average is not applicable
    
    total_quality_rating = completed_orders.aggregate(total=Sum('quality_rating'))['total'] or 0
    quality_rating_avg = total_quality_rating / total_completed_orders
    return round(quality_rating_avg, 2)

