"""
urls.py
Written by: Cameron Napoli
"""

from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^v1/', include('phone_verif.urls')),
    url(r'^administrator/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
]
