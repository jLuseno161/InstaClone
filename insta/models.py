from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=500, default="Bio", blank=True)
    
    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()  

    def search_profile(cls, user):
        return cls.objects.filter(user__username__icontains=user).all()

class Image(models.Model):
    img_name = models.CharField(max_length=80,blank=True)
    caption = models.CharField(max_length=600)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)
    image = CloudinaryField('images')

    def __str__(self):
        return self.img_name    

    def save_post(self):
        return self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search_post(cls, name):
        return cls.objects.filter(img_name__img__name__icontains=name)

    def post_likes(self):
        return self.likes.count()    


    