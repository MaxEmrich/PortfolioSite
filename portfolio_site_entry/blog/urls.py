from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # this is saying: when we go to the "" path on our webpage, go to the 'home' function in views and call that hoem function
]