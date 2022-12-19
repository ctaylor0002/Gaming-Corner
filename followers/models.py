from django.db import models
from authentication.models import User
from user_profile.models import UserProfile

# Create your models here.


class UserFollowers(models.Model):
    main_user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    