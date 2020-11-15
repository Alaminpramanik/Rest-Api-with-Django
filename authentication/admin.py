from django.contrib import admin

# Register your models here.
from rest_framework.authtoken.admin import User

User.raw_id_fields = ['user']