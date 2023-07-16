from django.contrib import admin
from .models import Income, AppUsers, Expense

# Register your models here.
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(AppUsers)