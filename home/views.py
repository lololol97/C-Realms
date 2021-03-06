from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

list = [User.objects.all()]

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html', {
                "users": list,
            })
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
