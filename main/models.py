from django.db import models
from django.contrib.auth.models import User
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class Customer(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, blank=True) 
    tc = models.CharField(max_length=11, validators=[RegexValidator(r'\d{11,11}',
            'TC. Kimlik Number must be 11 digits', 'Invalid number')], unique=True)
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)
    city = models.CharField(max_length=100, blank=False)
    district = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.tc + "\n" + self.name + "\n" + self.surname 
    