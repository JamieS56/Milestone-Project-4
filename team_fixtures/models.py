from django.db import models

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
    teams = models.ManyToManyField(Team)
    date_time = models.DateTimeField()
    home_team_goals = models.IntegerField(blank=True)
    away_team_goals = models.IntegerField(blank=True)

    def get_teams(self):

        return self.home_team, self.away_team

    def get_fixture_date(self):

        return self.date_time
