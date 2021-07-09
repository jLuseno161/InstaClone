from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.
# class Article(models.Model):
#     title = models.CharField(max_length=60)
#     post = models.TextField()
#     editor = models.ForeignKey(User,on_delete=models.CASCADE)
#     tags = models.ManyToManyField(tags)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     article_image = models.ImageField(upload_to='articles/', blank=True)

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=500)
    
