from django import forms
from App.models import Center

class CenterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = '__all__'
        exclude = ['status']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'operating_hours': forms.Select(attrs={'class': 'form-control'}),
            'number_of_slots_per_day': forms.NumberInput(attrs={'class': 'form-control'}),
        }