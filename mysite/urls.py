"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'), name='polls'),
    path('autos/', include('autos.urls'), name='autos'),
    path('authz/', include('authz.urls')),
]
