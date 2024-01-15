"""
URL's for accounts API's.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('change-password/', views.ChangePasswordApiView.as_view(), name='change-password'),
]
