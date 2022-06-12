"""turnitteal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from tealdb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.sites, name='main'),
    path('sites', views.sites, name='sites'),
    path('site/<int:site>', views.site, name='site'),
    path('sites/add', views.add_site, name='add_site'),
    path('sites/edit/<int:site>', views.edit_site, name='edit_site'),

    path('contacts', views.contacts, name='contacts'),
    path('contact/<int:contact>', views.contact, name='contact'),
    path('contacts/add', views.add_contact, name='add_contact'),
    path('contacts/edit/<int:contact>', views.edit_contact, name='edit_contact'),

    path('search', views.search, name='search'),
]
