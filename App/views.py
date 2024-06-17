from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CenterForm
from .models import Center
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