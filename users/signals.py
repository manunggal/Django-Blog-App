from django.db.models.signals import post_save # signal
from django.contrib.auth.models import User # sender
from django.dispatch import receiver # receiver
from .models import Profile # receiver


# signal: post_save
# sender: User
# receiver: create_profile
# kwargs: instance, created
# receiver: Profile
# kwargs: user
# action: create profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()