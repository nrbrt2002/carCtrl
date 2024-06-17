from django.db import models

CENTER_TYPE = (
    ('fixed', 'Fixed'),
    ('portable', 'Portable'),
)

WORKING_HOURS = (
    ('9:00 AM - 5:00 AM', '9:00 AM - 5:00 PM'),
    ('10:00 AM - 5:00 AM', '10:00 AM - 5:00 PM'),
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
    