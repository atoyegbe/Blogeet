from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Blog
from django.contrib.auth.models import Group 

def createProfile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='users')
        instance.groups.add(group)
        
        Profile.objects.create(
            user=instance,
            name=instance.username
            )
        



post_save.connect(createProfile, sender=User)   