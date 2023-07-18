from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Income, Expense

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required =True)

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

class PostIncome(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["incAmount", "category", "transaction_date"]

class PostExpense(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["expAmount", "category", "transaction_date"]
