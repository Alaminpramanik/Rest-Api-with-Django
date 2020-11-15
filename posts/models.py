from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    userid= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    title= models.CharField(max_length=100)
    body= models.CharField(max_length=500)
    


    def __str__(self):
        return self.title