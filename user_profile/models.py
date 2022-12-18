from django.db import models
from authentication.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


# class Car(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     make = models.CharField(max_length=30)
#     model = models.CharField(max_length=100)
#     year = models.IntegerField()

class User_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    profile_description = models.CharField(max_length=1000)
    #collection = models.ForeignKey(Collection, on_delete=models.CASCADE) (This will be used when I create the Colleciton App)
    #follewers = models.ForeignKey(Followers, on_delete=models.CASCADE) (This will be used when I create the Followers App)
    