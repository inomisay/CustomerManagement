from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["tc", "name", "surname", "phoneNumber", "city", "district"]
        
class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["tc", "name", "surname", "phoneNumber", "city", "district"]
        