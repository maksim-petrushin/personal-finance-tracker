from django.urls import path
from . import views

urlpatterns = [
    path("", views.index1, name="index1"),
    path("<int:user_id>", views.user, name="user")
    
]