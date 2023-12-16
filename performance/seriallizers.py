# performance/serializers.py
from rest_framework import serializers
from .models import VendorPerformance

class VendorPerformanceMetricsSerializer(serializers.Serializer):
    on_time_delivery_rate = serializers.FloatField()
    quality_rating_avg = serializers.FloatField()
    average_response_time = serializers.FloatField()
    fulfillment_rate = serializers.FloatField()
