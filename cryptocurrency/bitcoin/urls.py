"""
Bitcoin app URL's.
"""
from django.urls import path

from . import views

app_name = 'bitcoin'

urlpatterns = [
    path('', views.bitcoin_chart, name='bitcoin'),
]
