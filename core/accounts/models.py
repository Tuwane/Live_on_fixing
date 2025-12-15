from django.db import models
from django.contrib.auth import authenticate, login

# Create your models here.
class Sites(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Guard(models.Model):
    first_name = models.CharField(max_length=50)    
    last_name = models.CharField(max_length=50)    
    phone = models.CharField(max_length=50)    
    
    
    sites = models.ManyToManyField(
        Sites,
        related_name='guards',
        blank='True'
    )
    is_active = models.BooleanField(default=True)
    
    
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
    