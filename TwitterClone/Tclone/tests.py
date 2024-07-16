from django.contrib.auth.models import User
from django.test import TestCase
from .models import Bolt,Profile

class ProfileMethodTests(TestCase):

    def test_ensure_likes_default_0(self):
         # Create a test user & Bolt
        user = User.objects.create(username='testuser')
        bolt = Bolt.objects.create(user=user, body='This is a test bolt')
        
        self.assertEquals(bolt.get_number_likes(), 0)
    
    def test_ensure_user_follows_self(self):
         #test that a new created user will follow itself
         user = User.objects.create(username='testuser')
         user_profile, created = Profile.objects.get_or_create(user=user)

         self.assertEquals(user_profile.followed_by.count(), 1)

    def test_ensure_likes_increase(self):
        # Create a test user & Bolt
        user = User.objects.create(username='testuser')
        bolt = Bolt.objects.create(user=user, body='This is a test bolt')
            
        # Add likes to the Bolt instance
        bolt.likes.add(user)

        self.assertEquals(bolt.get_number_likes(), 1)

    def test_ensure_followers_increase(self):
            # Create 2 test users
            target_user = User.objects.create(username='targetuser')
            user = User.objects.create(username='testuser2')
            
            # Access the profiles
            target_profile, created = Profile.objects.get_or_create(user=target_user)
            user_profile, created = Profile.objects.get_or_create(user=user)
            
            # Add the follower
            target_profile.followed_by.add(user_profile)
            
            # Ensure the number of followers has increase by 1 (2 at current build users auto follow themseleves)
            self.assertEquals(target_profile.followed_by.count(), 2)
        
    def test_ensure_following_increase(self):
              # Create 2 test users
            target_user = User.objects.create(username='targetuser')
            user = User.objects.create(username='testuser2')
            
            # Access the profiles
            target_profile, created = Profile.objects.get_or_create(user=target_user)
            user_profile, created = Profile.objects.get_or_create(user=user)
            
            # Add the follower
            target_profile.followed_by.add(user_profile)
            
            # Ensure the number of followers has increase by 1 (2 at current build users auto follow themseleves)
            self.assertEquals(user_profile.follows.count(), 2)