from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import check_password as django_check_password, make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

CENTER_TYPE = (
    ('fixed', 'Fixed'),
    ('portable', 'Portable'),
)

WORKING_HOURS = (
    ('9:00 AM - 5:00 AM', '9:00 AM - 5:00 PM'),
    ('10:00 AM - 5:00 AM', '10:00 AM - 5:00 PM'),
)

STATUS=(
    ('pendig', 'Pendig'),
    ('done', 'Done'),
    ('cancled', 'Cancled'),
)
phone_regex = RegexValidator(
    regex=r'^\+250\d{9}$',
    message="Phone number must be entered in the format: '+250999999999'. Up to 12 digits allowed."
)

plate_regex = RegexValidator(
    regex=r'^[A-Z]{3} [0-9]{3} [A-Z]$',
    message="Plate number needd to be formated like AAA 000 A"
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
    

class OwnerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Owner(AbstractBaseUser, PermissionsMixin):
    names = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = OwnerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['names']

    def __str__(self):
        return f"{self.names} - {self.email} - {self.phone_number}"
    
    
    
class Car(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    model = models.TextField(max_length=50)
    make = models.TextField(max_length=50)
    plate = models.CharField(validators=[plate_regex], max_length=9, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.owner_id.names} - {self.make} - {self.model} - {self.plate}"
    
class Appointment(models.Model):
    date = models.DateField()
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    center_id = models.ForeignKey(Center, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='pendig')
    pstatus = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.owner_id.names} - {self.date} - {self.center_id.name} - {self.status}"