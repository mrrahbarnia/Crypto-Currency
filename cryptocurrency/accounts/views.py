from django.shortcuts import render # noqa

# Create your views here.

def login(request):

    return render(request, 'accounts/login.html')


def registration(request):

    return render(request, 'accounts/registration.html')
