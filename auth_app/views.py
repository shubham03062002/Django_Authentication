# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.backends import ModelBackend


def register_view(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            messages.success(req, "Registration successful.")
            return redirect('dashboard')  # Redirect to the dashboard or home
    else:
        init = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial =init)
        
    return render(req, 'auth/register.html', {'form': form})

def login_view(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('dashboard')  # Ensure this points to the correct URL name
        else:
            messages.error(req, "Invalid credentials.")
    return render(req, 'auth/login.html')

def logout_view(req):
    logout(req)
    messages.success(req, "You have been logged out.")
    return redirect('login')  # Redirect to login page or home

def dashboard(req):
    return render(req, 'auth/dashboard.html')  # Create a dashboard.html template
