from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.body

    location = models.CharField(max_length=100)
    body = models.TextField()
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    image = models.ImageField(upload_to='images/', blank=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')
    hashtag_field = models.CharField(max_length=200, blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    nickname = models.CharField(max_length=20)

class Comment(models.Model):
    def __str__(self):
        return self.text
            
    c_writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='c_writer', default="")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

class Hashtag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)