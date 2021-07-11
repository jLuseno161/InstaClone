from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=500, default="Bio", blank=True)

class Image(models.Model):
    img_name = models.CharField(max_length=80,blank=True)
    caption = models.CharField(max_length=600)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)
    image = CloudinaryField('images')
