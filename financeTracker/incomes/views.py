from django.shortcuts import render
from django.http import HttpResponse
from .models import Income

# Create your views here.

def index(request):
    return render(request, "incomes/index.html",{
        "incomes": Income.objects.all()
    })


def greet(request, name):
    return render(request, "incomes/greet.html",{
        "name" : name.capitalize()
    })
