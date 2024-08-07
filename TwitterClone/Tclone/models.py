from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    profile_image= models.ImageField(null=True,blank=True,upload_to="images/")
    profile_bio = models.CharField(null=True, blank=True, max_length=500)

    data_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username

#force profile to be made on user sign up 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    #when instance created assign it to profiles user feild
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        #follow self 
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

#tweeting model 
class Bolt(models.Model):
    user = models.ForeignKey(
        User, related_name='bolts',
        on_delete=models.DO_NOTHING
        )
    body = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="BoltLikes")

    def get_number_likes(self):
        return self.likes.count()

    def __str__(self):
        return(
            f"{self.user}, "
            f"{self.body}... "
            f"({self.created_at:%d/%m/%Y-%H:%M}): "
            )
    
class SharedBolt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bolt = models.ForeignKey(Bolt, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} shared {self.bolt}"

