from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CenterForm, OwnerForm, LoginOwnerForm
from .models import Center, Owner
from django.contrib.auth.hashers import make_password
from django.db import transaction
# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    form = LoginOwnerForm()
    if request.method == 'POST':
        form = LoginOwnerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Owner.objects.get(email=email)
                if user.check_password(password):
                    login(user)
                    return redirect('owner-dashboard')
                else:
                    form.add_error('password', 'Invalid password.')
            except Owner.DoesNotExist:
                form.add_error('email', 'Email not registered. create account Insted')
    context = {'form': form}
    return render(request, 'login-owner.html', context)


def signUp(request):
    form = OwnerForm()
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            if password != request.POST.get('cpassword'):
                form.add_error('password', 'Passwords do not match.')
            else:
                hashed_password = make_password(password)
                owner = form.save(commit=False)
                owner.password = hashed_password
                form.save()
                messages.success(request, "Account created successfuly. Now login") 
                return redirect('loginc')  
        else:
            messages.error(request, f"{form.errors.as_text}")
    context = {'form': form}
    return render(request, 'sign-up-owner.html', context)


def owner_dashboard(request):
    return render(request, 'owner-dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

@login_required
def center(request):
    centers = Center.objects.all()
    form = CenterForm()
    
    if request.method == 'POST':
        form = CenterForm(request.POST)
        if form.is_valid():
            center = form.save()
            messages.success(request, "New Inspection Center Created")
            form = CenterForm()
        else:
            messages.error(request, f"{form.errors.as_text}")    
    contex = {'form': form, 'centers': centers}
    return render(request, 'center.html', contex)


@login_required
def updateCenter(request, pk):
    centers = Center.objects.all()
    center = Center.objects.get(id=pk)
    form = CenterForm(instance=center)
    
    if request.method == 'POST':
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            messages.success(request, "Inspection Center Updated")
            return redirect("center")
        else:
            messages.error(request, f"{form.errors.as_text}")    
    contex = {'form': form, 'centers': centers}
    return render(request, 'update-center.html', contex)



@login_required
def deleteCenter(request, pk):
    center = Center.objects.get(id=pk)
    center.delete()
    messages.success(request, f"{center.name} Deleted Successfuly")
    return redirect('center')