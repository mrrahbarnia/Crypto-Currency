from django.urls import path

from . import views

urlpatterns = [
    path('', views.bitcoin_chart, name='bitcoin'),
]
