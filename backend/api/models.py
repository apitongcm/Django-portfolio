from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    imgLink = models.TextField( null=True, blank=True)
    title = models.CharField(max_length=200)
    badge = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"