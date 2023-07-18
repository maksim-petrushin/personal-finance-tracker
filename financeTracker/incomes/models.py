from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User  

# Create your models here.

class Income(models.Model): 
    INCOME = "IN"
    EXPENSE = "EX"
    TRANSACTION_CHOICES = [
            (INCOME, "Income"),
            (EXPENSE, "Expense")
        ]
    transaction_category = models.CharField(
        max_length=2,
        choices=TRANSACTION_CHOICES,
        default=INCOME,
    )
    person = models.ForeignKey(User, on_delete=models.PROTECT, related_name="pluses", blank=False, null=True)
    incAmount = models.FloatField(default=0)
    category = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
    transaction_date = models.DateTimeField(default=None)

    def __str__(self):
        return f"ID: {self.id} | AMOUNT: ${self.incAmount}| CATEGORY: {self.category}"
    
