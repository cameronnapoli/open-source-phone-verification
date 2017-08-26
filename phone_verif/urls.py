from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send_number/', views.index, name='send_number'),
    url(r'^verify_code/', views.index, name='verify_code'),
]
