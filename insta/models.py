from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=500, default="Bio", blank=True)
    
    def __str__(self):
            # return f'{self.user.username} Profile'

        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()  

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)
    
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()



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
    
    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image
        
    def post_likes(self):
        return self.likes.count()    

class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(Image, on_delete=models.CASCADE)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.user.user} Image'

    def save_comment(self):
        self.user

    def delete_comment(self):
        self.delete()



    