from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
   return render(request, 'login.html')


@login_required
def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

@login_required
def center(request):
   return render(request, 'center.html')