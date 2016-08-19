from django.forms import ModelForm
from .models import UsMessages

class MessageUser(ModelForm):
    class Meta:
        model = UsMessages
        fields = ['message_text']

