from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.body

    location = models.CharField(max_length=100)
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)