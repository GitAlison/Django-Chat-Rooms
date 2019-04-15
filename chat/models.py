from django.contrib.admin import models
from django.db import models
from django.conf import settings
# Create your models here.

class Room(models.Model):
    name = models.CharField('Name',max_length=20)
    created_at = models.DateTimeField('Created at',auto_now_add=True)
    updated_at = models.DateTimeField('Updated at',auto_now=True)

class Message(models.Model):
    room = models.ForeignKey(Room,null=True,blank=True,on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='sender',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


