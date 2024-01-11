"""
URL's for bitcoin API's.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BitCoinApiView.as_view(), name='bitcoin-api'),
]
