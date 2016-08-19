from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^logout/$', views.logout),
        url(r'^register/$', views.register),
        url(r'^index', views.login),
        url(r'^$', views.login),
]
