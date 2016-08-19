from django.db import models

class Records(models.Model):
    class Meta:
        db_table = "records"
    records_inuser_id = models.IntegerField()  #Кто написал
    records_user_id = models.IntegerField(default=0)     #Кому написали
    records_user_first = models.TextField()     #Имя кто написал
    records_user_last = models.TextField()      #Фамилия кто написал
    records_text = models.TextField(verbose_name="Запись") #текст
    records_date = models.DateTimeField()   #Дата публикации
    records_likes_id = models.TextField()   #айди кто лайкал
    records_likes = models.IntegerField(default=0) #количество лайков
    records_repost = models.IntegerField(default=0)    #количество репостов
    records_repost_id = models.TextField() #кто репостил

    repost_repost_user_id = models.IntegerField(null=True) #Кто сделал репост
    repost_repost_first = models.TextField(default='')    #Имя кто сделал репост
    repost_repost_last = models.TextField(default='') #Фамилия кто сделал репост
    repost_repost_date = models.DateTimeField(null=True)  # дата репоста

    repost_repost_likes_id = models.TextField(default='')  # Лайки репоста, айди
    repost_repost_likes = models.IntegerField(default=0)  # Количество лайков

    repost_repost = models.IntegerField(default=0)  #Репост репоста, количество
    repost_repost_id = models.TextField(default='')   #Айди кто сделал репост


class Comments(models.Model):
    class Meta:
        db_table = "comments"
    comments_records_id = models.IntegerField() #Айди записи, которую коментируют

    comments_users_id = models.IntegerField() #Айди коментатора
    comments_users_first = models.TextField() #Имя коментатора
    comments_users_last = models.TextField() #фамилия коментатора
    comments_users_date = models.DateTimeField() #дата коментария
    comments_users_text = models.TextField(verbose_name="Комментарий") #текст коментария
    comments_users_like_id = models.TextField(default="") #айди, кто лайкал
    comments_users_like = models.IntegerField(default=0) #лайки

    answer_users_id = models.IntegerField(null=True) #айди кто ответил
    answer_users_first = models.TextField(default="") #имя кто ответил
    answer_users_last = models.TextField(default="") #фамилия кто ответил
    answer_users_date = models.DateTimeField(null=True) #дата
    answer_users_text = models.TextField(default="") #текст
    answer_users_like_id = models.TextField(default="") #кто лайкнул ответ
    answer_users_like = models.IntegerField(default=0) #лайки ответа

class PhotoAlbom(models.Model):
    class Meta:
        db_table = "albomphoto"
    abpho_user_id = models.IntegerField(default=0)
    abpho_user_albom_id = models.IntegerField(default=0)
    abpho_user_photo = models.ImageField(upload_to='static/photo')
    abpho_user_photo_date = models.DateTimeField(null=True) #дата
    abpho_user_photo_like_id = models.TextField(default='')
    abpho_user_photo_like = models.IntegerField(default=0)
    abpho_user_photo_ava = models.IntegerField(default=0)













