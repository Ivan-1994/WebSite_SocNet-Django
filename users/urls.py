from django.conf.urls import url
from . import views
from django.contrib import auth


urlpatterns = [
        url(r"^albompho", views.albompho),
        url(r"^delphoto(?P<id_f>\d+)", views.delphoto),

        url(r"^bdrecords(?P<user_id>\d+)", views.bdrecords),
        url(r"^addcomment(?P<rec_id>\d+)/(?P<user_id>\d+)", views.addcomment),
        url(r"^all_users", views.allusers),

        url(r"^addlike(?P<like_id>\d+)", views.addlike),
        url(r"^addlikere(?P<like_id>\d+)", views.addlikere),
        url(r"^addlikecom(?P<like_id>\d+)/(?P<user_id>\d+)", views.addlikecom),

        url(r"^killlike(?P<like_id>\d+)", views.killlike),
        url(r"^killlikere(?P<like_id>\d+)", views.killlikere),
        url(r"^killlikecom(?P<like_id>\d+)/(?P<user_id>\d+)", views.killlikecom),

        url(r"^addrepost(?P<rec_id>\d+)", views.addrepost),
        url(r"^delpost(?P<pol_id>\d+)", views.delpost),
        url(r"^id(?P<user_id>\d+)", views.index),
]
