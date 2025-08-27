from rest_framework import serializers
from .models import Post, Contact
from datetime import datetime

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)  
    #created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_username', 'created_at', 'badge', 'imgLink', 'link']
    

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Contact
        fields =['name','email','message']
     