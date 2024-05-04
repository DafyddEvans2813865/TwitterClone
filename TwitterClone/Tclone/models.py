from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username

#force profile to be made on user sign up 
def create_profile(sender, instance, created, **kwargs):
    #when instance created assign it to profiles user feild
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        #follow self and myself
        user_profile.follows.set([instance.profile.id,User.objects.get(username='evans').id])
        user_profile.save()

post_save.connect(create_profile, sender=User)