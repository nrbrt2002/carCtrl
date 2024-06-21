from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import Owner

class EmailBackendForOwners(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Owner.objects.get(email=email)
        except Owner.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Owner.objects.get(pk=user_id)
        except Owner.DoesNotExist:
            return None

class EmailBackendForAdmins(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
