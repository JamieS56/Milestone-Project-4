from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history.
    This Class is not actually used, but still needs
    to exist for migration purposes.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
