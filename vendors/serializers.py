# vendors/serializers.py

from .models import Vendor
from rest_framework import serializers

class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = ['name', 'contact_details', 'address', 'vendor_code']
