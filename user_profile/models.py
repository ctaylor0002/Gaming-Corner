from django.db import models
from authentication.models import User
from video_game.models import Video_Game

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


# class Car(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     make = models.CharField(max_length=30)
#     model = models.CharField(max_length=100)
#     year = models.IntegerField()

class User_Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_game = models.ForeignKey(Video_Game, on_delete=models.CASCADE)

class User_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    profile_description = models.CharField(max_length=1000)
    collection = models.ForeignKey(User_Collection, on_delete=models.CASCADE, default=None)
    #follewers = models.ForeignKey(Followers, on_delete=models.CASCADE) (This will be used when I create the Followers App)


