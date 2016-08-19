from django.db import models

class UsMessages(models.Model):
    class Meta:
        db_table = "usmessages"
    message_user_id = models.IntegerField(default=0)
    message_user_name = models.TextField(default='')
    message_outuser_id = models.IntegerField(default=0)
    message_outuser_name = models.TextField(default='')
    message_text = models.TextField(default='')
    message_date = models.DateTimeField(default=0)
    message_name = models.IntegerField(default=0)
    message_see = models.IntegerField(default=0)