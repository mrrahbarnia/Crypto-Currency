"""
Views for Bitcoin app.
"""
from django.shortcuts import render


def bitcoin_chart(request):

    return render(request, 'bitcoin/chart.html')
