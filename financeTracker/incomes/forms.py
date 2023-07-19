from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Income
from django.db import models

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required =True)

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

class PostIncome(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["incAmount","transaction_category", "transaction_date"]
        widgets = {'transaction_date' : DateInput()}
    
