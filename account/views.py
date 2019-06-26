from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def join(request):
    if request.method== "GET":
        return render(request, "join.html")
    elif request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        password_again=request.POST['password_again']
        if password != password_again:
            return render(request, "join.html")
        user=User.objects.create_user(username=username, password=password)
        auth.login(request, user)
    return redirect("home")

def login(request):
    if request.method=="GET":
         return render(request, "login.html")
    elif request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user =auth.authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "login.html")
        auth.login(request, user)
    return redirect("home")