from django.urls import path
from . import views

urlpatterns = [
    path("", views.index1, name="index1"),
    path("home", views.index1, name="index1"),
    path("<int:user_id>", views.user, name="user"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("create-income", views.create_income, name="create-income"),
    path("create-expense", views.create_expense, name="create-expense")
]