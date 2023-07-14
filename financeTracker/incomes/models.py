from django.db import models
from datetime import datetime    

# Create your models here.
class AppUsers(models.Model):
    first= models.CharField(max_length=64, blank=False)
    last = models.CharField(max_length=64,blank=False)

    def __str__(self):
        return f"name: {self.first} {self.last}"


class Income(models.Model): 
    person = models.ForeignKey(AppUsers, on_delete=models.PROTECT, related_name="pluses", blank=False, null=True)
    incAmount = models.FloatField(default=0)
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"ID: {self.id} | AMOUNT: ${self.incAmount}| CATEGORY: {self.category}"
    
