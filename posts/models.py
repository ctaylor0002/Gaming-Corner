from django.db import models
from authentication.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_content = models.CharField(max_length=1000)
    likes = models.IntegerField()
    dislikes = models.IntegerField()