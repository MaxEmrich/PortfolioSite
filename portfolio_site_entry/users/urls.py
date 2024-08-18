from django.urls import path, include
from .views import RegisterView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'), # this "include" function takes everything that comes AFTER the stuff inside "/" and passes it to the blog.urls file
]
