from django import forms
from App.models import Center, Owner, Car

class CenterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = '__all__'
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'operating_hours': forms.Select(attrs={'class': 'form-control'}),
            'number_of_slots_per_day': forms.NumberInput(attrs={'class': 'form-control'}),
        }
class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
        exclude = ['is_active', 'is_staff', 'last_login', 'groups', 'is_superuser', 'user_permissions']
        widgets = {
            'names': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'value': "+250", 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
class LoginOwnerForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['owner_id']
        widgets = {
            'plate': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
        }
        