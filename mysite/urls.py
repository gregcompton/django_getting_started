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
    path('', include('home.urls'), name='sitehome'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    # path('oauth/', include('social_django.urls', namespace='social')),

    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'), name='polls'),
    path('autos/', include('autos.urls'), name='autos'),
    path('authz/', include('authz.urls')),
    path('form/', include('form.urls')),
    path('myarts/', include('myarts.urls')),
    path('crispy/', include('crispy.urls')),
    path('home/', include('home.urls')),
    path('menu/', include('menu.urls')),
    path('chat/', include('chat.urls')),

]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve,
            {'document_root': os.path.join(BASE_DIR, 'site'),
             'show_indexes': True},
            name='site_path'
            ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
        'path': 'favicon.ico',
        'document_root': os.path.join(BASE_DIR, 'mysite/static'),
        # 'document_root': os.path.join(BASE_DIR, ''),
    }
         ),
]
