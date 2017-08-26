from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send_number/$', views.send_number, name='send_number'),
    url(r'^verify_code/$', views.verify_code, name='verify_code'),
]
