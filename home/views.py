from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

