from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('admin-dashboard', views.admin_dashboard, name = "admin-dashboard"),
    path('dashboard/center', views.center, name="center"),
    # path('login', views.login, name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]

