from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin_in_ass/', admin.site.urls),
    url(r'^', include('users.urls')),
    url(r'^', include('loginsys.urls')),
    url(r'^', include('usmessages.urls')),
]
