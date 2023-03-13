from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm 

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=200,required=False)
    last_name = forms.CharField(max_length=200,required=False)
    email = forms.EmailField(required=False)
    # class Meta:
    #     model = User
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude =("user",)