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
from django.conf.urls import url
from django.contrib import admin

from tealdb import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.sites, name='main'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^contacts/([0-9]+)$', views.contact, name='contact'),
    url(r'^contacts/add$', views.add_contact, name='add_contact'),
    url(r'^sites$', views.sites, name='sites'),
    url(r'^sites/([0-9]+)$', views.site, name='site'),
    url(r'^sites/add$', views.add_site, name='add_site'),
    url(r'^search$', views.search, name='search'),
]
