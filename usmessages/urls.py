from django.conf.urls import url
from . import views


urlpatterns = [
        url(r"^messages", views.usmessages),
        url(r"^message(?P<user_id>\d+)", views.usmessage),
        url(r"^addmessage(?P<user_id>\d+)", views.addmessage),
]
