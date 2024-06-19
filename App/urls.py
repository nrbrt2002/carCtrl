from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="loginc"),
    path('sign-up/', views.signUp, name="sign-upc"),
    
    
    path('owner-dashboard', views.owner_dashboard, name="owner-dashboard"),
    
    path('admin-dashboard', views.admin_dashboard, name = "admin-dashboard"),
    path('dashboard/center', views.center, name="center"),
    path('dashboard/center/delete/<int:pk>/', views.deleteCenter, name="delete-center"),
    path('dashboard/center/edit/<int:pk>/', views.updateCenter, name="update-center"),
    
    # path('login', views.login, name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
]

