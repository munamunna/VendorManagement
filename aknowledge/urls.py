from django.urls import path
from .views import acknowledge_purchase_order

urlpatterns = [
    
    path('purchase_orders/<int:po_id>/aknowledge/', acknowledge_purchase_order, name='acknowledge_purchase_order'),
]
