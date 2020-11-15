from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
       # fields= ['userid', 'id', 'title','body']
        fields= '__all__'
       

