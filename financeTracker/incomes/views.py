from django.shortcuts import render
from django.http import HttpResponse
from .models import Income, AppUsers, Expense

# Create your views here.
 
def index1(request):
    return render(request, "incomes/index.html",{
        "appusers": AppUsers.objects.all()
    })
def user(request, user_id):
    user = AppUsers.objects.get(pk=user_id)
    return render(request, "incomes/user.html",{
        "incomes": user.pluses.all(),
        "expenses": user.minuses.all()
    })
 

