from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Income, AppUsers, Expense
from .forms import RegisterForm, PostIncome
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def create_income(request):
    if request.method == 'POST':
        form = PostIncome(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.person = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostIncome()
    return render(request, 'incomes/create_income.html', {"form":form})


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
        "appusers": User.objects.all()
    })

def user(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "incomes/user.html",{
        "incomes": user.pluses.all(),
        "expenses": user.minuses.all(),
        "sumInc": incomeSum(user_id),
        "sumExp": expenseSum(user_id),
        "sumNet": netSum(user_id)
    })

def incomeSum(user_id):
    sum = 0
    user = User.objects.get(pk=user_id).pluses.all()
    for expense in user:
        sum+=expense.incAmount
    return sum

def expenseSum(user_id):
    sum = 0
    user = User.objects.get(pk=user_id).minuses.all()
    for expense in user:
        sum+=expense.expAmount
    return sum

def netSum(user_id):
    return incomeSum(user_id)-expenseSum(user_id)


