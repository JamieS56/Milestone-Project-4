from django.db import models
from django import forms

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=20)
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    points = models.IntegerField()



class Fixture(models.Model):
    teams = models.ManyToManyField(Team)
    date_time = forms.SplitDateTimeField()
    home_team_goals = models.IntegerField(blank=True)
    away_team_goals = models.IntegerField(blank=True)

    def get_teams(self):

        return self.home_team, self.away_team

    def get_fixture_date(self):

        return self.date_time
