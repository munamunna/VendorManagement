
from rest_framework.authtoken.models import Token


from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from .models import CustomUser


@api_view(['POST'])
def user_registration(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def user_login(request):
    """
    Try to login a user
    """
    data = request.data

    try:
        username = data['username']
        password = data['password']
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # Use authenticate method to check the credentials
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Authentication successful, retrieve or create a token
        user_token, created = Token.objects.get_or_create(user=user)
        data = {'token': user_token.key}
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        # Authentication failed
        return Response(status=status.HTTP_401_UNAUTHORIZED)
