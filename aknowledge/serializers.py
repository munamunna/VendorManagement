from rest_framework import serializers

class AcknowledgePurchaseOrderSerializer(serializers.Serializer):
    acknowledgment_date = serializers.DateTimeField(required=False,allow_null=True)

