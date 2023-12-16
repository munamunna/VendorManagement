
from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated,IsAdminUser

# from .models import Vendor
# from .serializers import VendorSerializer

# class VendorsViewSet(viewsets.ModelViewSet):
#     authentication_classes = [TokenAuthentication]  
#     permission_classes = [IsAdminUser] 
    
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

  
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission,IsAuthenticated, IsAdminUser

from .models import Vendor
from .serializers import VendorSerializer

class VendorPermissionClass(BasePermission):
    def has_permission(self, request, view):
        # Allow any authenticated user to list vendors
        if view.action in ['list','retrieve']:
            return request.user and request.user.is_authenticated
        # Allow only admin users to create or update vendors
        elif view.action in ['create', 'update']:
            return request.user and request.user.is_authenticated and request.user.is_staff
        return True

class VendorsViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [VendorPermissionClass]

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def perform_create(self, serializer):
        # Customize the creation of a new vendor if needed
        serializer.save()

    def perform_update(self, serializer):
        # Customize the update of an existing vendor if needed
        serializer.save()


