"""
Views for Bitcoin app.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def bitcoin_chart(request):

    return render(request, 'bitcoin/chart.html')
