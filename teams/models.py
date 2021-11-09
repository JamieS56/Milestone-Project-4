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
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    home_team_goals = models.IntegerField(null=True, blank=True)
    away_team_goals = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    game_played = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.home_team} V {self.away_team}'
