from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Income, AppUsers, Expense
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
 
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {"form":form})

@login_required(login_url="/login")
def index1(request):
    return render(request, "incomes/index.html",{
        "appusers": AppUsers.objects.all()
    })
def user(request, user_id):
    user = AppUsers.objects.get(pk=user_id)
    return render(request, "incomes/user.html",{
        "incomes": user.pluses.all(),
        "expenses": user.minuses.all(),
        "sumInc": incomeSum(user_id),
        "sumExp": expenseSum(user_id),
        "sumNet": netSum(user_id)
    })

def incomeSum(user_id):
    sum = 0
    user = AppUsers.objects.get(pk=user_id).pluses.all()
    for expense in user:
        sum+=expense.incAmount
    return sum

def expenseSum(user_id):
    sum = 0
    user = AppUsers.objects.get(pk=user_id).minuses.all()
    for expense in user:
        sum+=expense.expAmount
    return sum

def netSum(user_id):
    return incomeSum(user_id)-expenseSum(user_id)


