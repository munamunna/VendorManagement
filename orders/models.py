from django.db import models

# Create your models here.

from django.db import models

from vendors.models import Vendor
from jsonfield import JSONField


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = JSONField()
    quantity = models.IntegerField()
    options = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    )
    status = models.CharField(max_length=20, choices=options, default="pending")
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO#{self.po_number} - {self.vendor.name}"

