from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Goal


@receiver(post_save, sender=Goal)
def save_goal(sender, instance, created, **kwargs):
    """
    Listen for when a Goal is saved
    """

    return True


@receiver(post_save, sender=Goal)
def create_goal(sender, instance, created, **kwargs):
    if created:
        Goal.objects.create(goal=instance)

