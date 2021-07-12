from django.test import TestCase

from .models import Comment, Profile, Image
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    """Test for the profile model class"""
    def setUp(self):
        self.user = User(username='joy')
        self.user.save()

        self.profile = Profile(id=1, profile_pic='profile.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

class ImageTestClass(TestCase):
    """
    test class for Image model unit tests.
    """
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.new_profile = Profile(profile_pic='profile.png',bio='this is a test profile',user=self.user)
        self.new_profile.save()
        self.newImage = Image(image='profile.png',caption="image", profile=self.new_profile)

    def test_instance_true(self):
        self.assertTrue(isinstance(self.newImage, Image))

    def test_save_post(self):
        self.newImage.save_post()
        img = Image.objects.all()
        self.assertTrue(len(img) == 1)

    def test_delete_post(self):
        self.newImage.save_post()
        img = Profile.objects.all()
        self.assertTrue(len(img) <= 1)
        
class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User(username='joy')
        self.user.save()

        self.new_profile = Profile(profile_pic='profile.png',bio='this is a test profile',user=self.user)
        self.new_profile.save()
        self.newImage = Image(image='profile.png',caption="image", profile=self.new_profile)
        self.comment = Comment(id=1, comment='bla bla bla', user=self.new_profile, post = self.newImage, date="23-01-2020")

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.comment.save_comment()
        comment = Comment.objects.all()
        self.assertFalse(len(comment) > 1)

    def test_delete_comment(self):
        self.comment.delete_comment()
        comment = Comment.objects.all()
        self.assertTrue(len(comment)  <= 1)



