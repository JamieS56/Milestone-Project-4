from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

from teams.models import Fixture


class UserProfile(models.Model):
    """
    A user profile model for maintaining order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username
