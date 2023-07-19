from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Income
from .forms import RegisterForm, PostIncome
from django.contrib.auth import login
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

    transactions = Income.objects.filter(person=request.user)
    return render(request, "incomes/index.html",{"transactions": transactions})

