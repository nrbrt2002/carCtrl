from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CenterForm, OwnerForm, LoginOwnerForm, CarForm
from .models import Center, Owner, Car
from django.contrib.auth.hashers import make_password
from django.db import transaction
# Create your views here.

def home(request):
    return render(request, 'index.html')

def owner_login_view(request):
    if request.method == 'POST':
        form = LoginOwnerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('owner-dashboard')  # Redirect to a home page or dashboard
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginOwnerForm()

    return render(request, 'login-owner.html', {'form': form})


def admin_login_view(request):
    if request.method == 'POST':
        form = LoginOwnerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password, backend='yourapp.backends.EmailBackendForAdmins')
            if user is not None:
                login(request, user, backend='yourapp.backends.EmailBackendForAdmins')
                return redirect('admin_dashboard')  # Redirect to the admin's dashboard
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginOwnerForm()

    return render(request, 'admin-login.html', {'form': form})


@login_required(login_url='loginc')
def owner_logout_view(request):
    logout(request)
    return redirect('home') 

def signUp(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        confirm_password = request.POST.get('cpassword')
        if form.is_valid():
            password = form.cleaned_data.get('password')
            if password != confirm_password:
                form.add_error('password', 'Passwords do not match.')
            else:
                owner = form.save(commit=False)
                owner.set_password(password)
                owner.save()
                login(request, owner)
                return redirect('loginc') 
    else:
        form = OwnerForm()
    context = {'form': form}
    return render(request, 'sign-up-owner.html', context)


@login_required(login_url='loginc')
def owner_cars(request):
    form = CarForm()
    owner = Owner.objects.get(id = request.user.id)
    cars = Car.objects.filter(owner_id = owner.id)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner_id = owner
            car.save()
            messages.success(request, "Car Added To your Account")
            form = CarForm()
        else:
            messages.error(request, f"{form.errors.as_text}")
    context = {'form': form, 'cars': cars}
    return render(request, 'owner-cars.html', context)

@login_required(login_url='loginc')
def owner_cars_edit(request, pk):
    car = Car.objects.get(id=pk)
    owner = Owner.objects.get(id = request.user.id)
    cars = Car.objects.filter(owner_id = owner.id)
    form = CarForm(instance=car)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car.save()
            messages.success(request, "Car Updated")
            return redirect('owner-cars')
        else:
            messages.error(request, f"{form.errors.as_text}")
    context = {'form': form, 'cars': cars}
    return render(request, 'owner-cars-edit.html', context)


@login_required(login_url='loginc')
def owner_cars_delete(request, pk):
    car = Car.objects.get(id=pk)
    car.delete()
    messages.success(request, f"Car with Plate {car.plate} Deleted Successfuly")
    return redirect('owner-cars')

@login_required(login_url='loginc')
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