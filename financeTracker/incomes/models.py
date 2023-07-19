from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User


# Create your models here.


class Income(models.Model): 
    TRANSACTION_CHOICES = [
            ("1", "INCOME - Wages"),
            ("2", "INCOME - Salary"),
            ("3", "INCOME - Commission"),
            ("4", "INCOME - Interest"),
            ("5", "INCOME - Sale Profit"),
            ("6", "INCOME - Investments"),
            ("7", "INCOME - Gifts"),
            ("8", "INCOME - Allowance/Pocket Money"),
            ("9", "INCOME - Government Payments"),
            ("10","INCOME - Other"),
            ("11", "EXPENSE - Housing"),
            ("12", "EXPENSE - Utilities"),
            ("13", "EXPENSE - Vehicles/transportation"),
            ("14", "EXPENSE - Gas"),
            ("15", "EXPENSE - Groceries/essentials"),
            ("16", "EXPENSE - Internet/cable"),
            ("17", "EXPENSE - Cellphone"),
            ("18", "EXPENSE - Debt payments"),
            ("19", "EXPENSE - Memberships and subscriptions "),
            ("20", "EXPENSE - Child care"),
            ("21", "EXPENSE - Health care"),
            ("22", "EXPENSE - Emergency fund"),
            ("23", "EXPENSE - Retirement"),
            ("24", "EXPENSE - Travel"),
            ("25", "EXPENSE - Large purchases"),
            ("26", "EXPENSE - Other")
        ]
    transaction_category = models.CharField(
        max_length=26,
        choices=TRANSACTION_CHOICES,
        default="10",
    )
    person = models.ForeignKey(User, on_delete=models.PROTECT, related_name="pluses", blank=False, null=True)
    incAmount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
    transaction_date = models.DateTimeField(default=None)

    def __str__(self):
        return f"ID: {self.id} | AMOUNT: ${self.incAmount}| CATEGORY: {self.category}"
    
