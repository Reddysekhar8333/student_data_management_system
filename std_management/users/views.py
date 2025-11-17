from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")
