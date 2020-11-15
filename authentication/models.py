from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)   
    password= models.CharField(
        max_length=50)
    confirm_password= models.CharField(
        max_length=50)
    

    


    def __str__(self):
        return self.email  