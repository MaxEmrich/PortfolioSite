"""
URL configuration for portfolio_site_entry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Note: When a request comes in, django loops through the urlpatterns list, then stops at the first one that 
# matches the requested path in the url. The 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")), # this "include" function takes everything that comes AFTER the stuff inside "/" and passes it to the blog.urls file
    path("accounts/", include("users.urls")),
    path('tinymce/', include('tinymce.urls')),
]
