from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = "username", password = "password")
    else:
        return render(request, 'login.html')

    if user is not None:
        auth.login(request, user)
        return redirect("/")
    else:
        messages.error(request, 'invalid boboboy')
        return redirect("login")
