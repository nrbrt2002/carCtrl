from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('owner/login/', views.owner_login_view, name="loginc"),
    path('owner/sign-up/', views.signUp, name="sign-upc"),
    path('owner/logout/', views.owner_logout_view, name='logoutc'),

    path('adminstrator/login', views.admin_login_view, name="loginA"),
    
    path('owner-dashboard', views.owner_dashboard, name="owner-dashboard"),
    path('owner-dashboard/cars', views.owner_cars, name="owner-cars"),
    path('owner-dashboard/cars/edit/<int:pk>', views.owner_cars_edit, name="owner-cars-edit"),
    path('owner-dashboard/cars/delete/<int:pk>', views.owner_cars_delete, name="owner-cars-delete"),
    
    path('admin-dashboard', views.admin_dashboard, name = "admin-dashboard"),
    path('dashboard/center', views.center, name="center"),
    path('dashboard/center/delete/<int:pk>/', views.deleteCenter, name="delete-center"),
    path('dashboard/center/edit/<int:pk>/', views.updateCenter, name="update-center"),
    
    path("accounts/", include("django.contrib.auth.urls")),
]

