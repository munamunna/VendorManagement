# performance/urls.py
from django.urls import path
from .views import VendorPerformanceMetricsView

urlpatterns = [
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceMetricsView.as_view(), name='vendor-performance-metrics'),
]
