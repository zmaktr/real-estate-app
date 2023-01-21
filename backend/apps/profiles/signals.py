import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)

#@receiver(signal, **kwargs)
#def receiver_function(sender, instance, action, **kwargs)
@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("going to create profile instance")
        Profile.objects.create(user=instance)
        print("created Profile Instance")

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile created")
    print("Profile instance saved")