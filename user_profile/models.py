from django.db import models
from authentication.models import User
from video_game.models import VideoGame
# from followers.models import UserFollowers

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


# class Car(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     make = models.CharField(max_length=30)
#     model = models.CharField(max_length=100)
#     year = models.IntegerField()

class UserCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='../images/base_profile_picture.jpg')
    profile_description = models.CharField(max_length=1000)
    # collection = models.ForeignKey(UserCollection, on_delete=models.CASCADE, default=None)
    # user_profile_follewers = models.ManyToManyField(to='followers.UserFollowers')


