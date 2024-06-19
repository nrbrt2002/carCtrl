from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import check_password as django_check_password, make_password
CENTER_TYPE = (
    ('fixed', 'Fixed'),
    ('portable', 'Portable'),
)

WORKING_HOURS = (
    ('9:00 AM - 5:00 AM', '9:00 AM - 5:00 PM'),
    ('10:00 AM - 5:00 AM', '10:00 AM - 5:00 PM'),
)

phone_regex = RegexValidator(
    regex=r'^\+250\d{9}$',
    message="Phone number must be entered in the format: '+250999999999'. Up to 12 digits allowed."
)
# Create your models here.

class Center(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=CENTER_TYPE)
    operating_hours = models.CharField(max_length=50, choices=WORKING_HOURS)
    number_of_slots_per_day = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_at"]
    
    def __str__(self):
        return f"{self.name} - {self.location} - {self.operating_hours} - {self.number_of_slots_per_day}"
    
    def save(self, *args, **kwargs):
        if self.type == 'fixed':
            self.operating_hours = '9:00 AM - 5:00 AM'
        else:
            self.operating_hours = '10:00 AM - 5:00 AM'
        super(Center, self).save(*args, **kwargs)
    
class Owner(models.Model):
    names = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_at"]
    
    def __str__(self):
        return f"{self.names} - {self.email} - {self.phone_number}"
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return django_check_password(raw_password, self.password)