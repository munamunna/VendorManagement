# urls.py
from django.urls import path
from .views import user_login,user_registration

urlpatterns = [
    # Other URLs
    path('login/', user_login, name='user-login'),
    path('register/', user_registration, name='user-register'),
]
