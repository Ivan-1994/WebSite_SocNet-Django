from django.forms import ModelForm
from .models import Records, Comments, PhotoAlbom

class CommentForm(ModelForm):
    class Meta:
        model = Records
        fields = ['records_text']

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_users_text']

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()