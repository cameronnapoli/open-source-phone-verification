"""
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^verif/', include('phone_verif.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
]
