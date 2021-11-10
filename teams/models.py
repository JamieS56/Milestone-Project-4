from django.db import models
from django import forms
from django.shortcuts import get_object_or_404

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=20)
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return self.name


class Fixture(models.Model):

    HOME_OR_AWAY = [
        ('H', 'Home'),
        ('A', 'Away')
    ]



    home_or_away = models.CharField(max_length=1, choices=HOME_OR_AWAY)
    opposition_team = models.IntegerField(choices=Team.objects.values_list('id', 'name').exclude(name='Messi Ankles'))
    messi_ankles_team_goals = models.IntegerField(null=True, blank=True)
    opposition_team_goals = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    game_played = models.BooleanField(default=False)

