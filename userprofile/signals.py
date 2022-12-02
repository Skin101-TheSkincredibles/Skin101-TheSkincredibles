from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver #decorator catch the signal called post_save
from .models import Profile

# when a user saved, send the signals (post_save) and received by the sender. 
# **kwargs = accept any additional keyword arguments
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: # if user created
        Profile.objects.create(user=instance) # create a profile object, which user equals to instance -> run everytime user created

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()