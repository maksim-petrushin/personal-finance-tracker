from django.db import models
from datetime import datetime    

# Create your models here.

class Income(models.Model):
    incAmount = models.FloatField(default=0)
    description = models.CharField(max_length=512)
    category = models.CharField(max_length=64)
    incDate = models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return f"ID: {self.id} | AMOUNT: ${self.incAmount}| CATEGORY: {self.category} | DATE: {self.incDate} | DESCRIPTION: {self.description} | "