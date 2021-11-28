from django.db import models
from teams.models import Team
from players.models import Player


class Fixture(models.Model):

    """
    Stores a fixture that contains the teems that played in it, the date and
    the time of the fixture. Includes methods to retrieve goals in the
    fixture for both teams.
    """

    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='home_team',
        null=False,
        blank=False
        )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='away_team',
        null=False, blank=False
        )
    date = models.DateField()
    time = models.TimeField()
    game_played = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f'{self.date}: {self.home_team} v {self.away_team}'

    def home_team_goals(self):
        goals = Goal.objects.filter(fixture=self, team=self.home_team)
        return goals

    def away_team_goals(self):
        goals = Goal.objects.filter(fixture=self, team=self.away_team)
        return goals


class Goal(models.Model):
    """
    Store info about goals such as which team scored who scored, who assisted
    and which fixture it was scored in.
    """

    goal_id = models.CharField(max_length=100, primary_key=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='team_goals'
        )
    goal_scorer = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='goals',
        null=True,
        blank=True
        )
    assist_maker = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='assists',
        null=True,
        blank=True
        )
    fixture = models.ForeignKey(
        Fixture,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    def __str__(self):
        return f'Goal: {self.team}, {self.fixture}'
