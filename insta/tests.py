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


