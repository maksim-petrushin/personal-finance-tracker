from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User  

# Create your models here.
class AppUsers(models.Model):
    first= models.CharField(max_length=64, blank=False)
    last = models.CharField(max_length=64,blank=False)

    def __str__(self):
        return f"{self.first} {self.last}"


class Income(models.Model): 
    person = models.ForeignKey(User, on_delete=models.PROTECT, related_name="pluses", blank=False, null=True)
    incAmount = models.FloatField(default=0)
    category = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
    transaction_date = models.DateTimeField(default=None)

    def __str__(self):
        return f"ID: {self.id} | AMOUNT: ${self.incAmount}| CATEGORY: {self.category}"
    
class Expense(models.Model):
    person = models.ForeignKey(User, on_delete=models.PROTECT, related_name="minuses", blank=False, null=True)
    expAmount = models.FloatField(default=0)
    category = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
    transaction_date = models.DateTimeField(default=None)

    def __str__(self):
        return f"ID: {self.id} | AMOUNT: ${self.expAmount}| CATEGORY: {self.category}"
    
