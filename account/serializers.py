# serializers.py
# from rest_framework import serializers
from .models import CustomUser

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password', 'user_type']
        

from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'user_type']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            user_type=validated_data['user_type'],
            is_staff=(validated_data['user_type'] == 'admin')  # Set is_staff for admin users
        )
        return user
