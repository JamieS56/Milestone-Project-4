from django.db import models
from players.models import Player

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

    def id(self):
        return self.id

    def wins(self):
        wins = 0
        home_fixture_list = Fixture.objects.filter(game_played=True, home_team=self.id)
        for fixtures in home_fixture_list:
            if fixtures.home_team_goals > fixtures.away_team_goals:
                wins = wins + 1
            else:
                pass

        away_fixture_list = Fixture.objects.filter(game_played=True, away_team=self.id)
        for fixtures in away_fixture_list:
            if fixtures.away_team_goals > fixtures.home_team_goals:
                wins = wins + 1
            else:
                pass

        return wins

    def losses(self):
        losses = 0
        home_fixture_list = Fixture.objects.filter(game_played=True, home_team=self.id)
        for fixtures in home_fixture_list:
            if fixtures.home_team_goals < fixtures.away_team_goals:
                losses = losses + 1
            else:
                pass

        away_fixture_list = Fixture.objects.filter(game_played=True, away_team=self.id)
        for fixtures in away_fixture_list:
            if fixtures.away_team_goals < fixtures.home_team_goals:
                losses = losses + 1
            else:
                pass

        return losses

    def draws(self):
        draws = 0
        home_fixture_list = Fixture.objects.filter(game_played=True, home_team=self.id)
        for fixtures in home_fixture_list:
            if fixtures.home_team_goals < fixtures.away_team_goals:
                draws = draws + 1
            else:
                pass

        away_fixture_list = Fixture.objects.filter(game_played=True, away_team=self.id)
        for fixtures in away_fixture_list:
            if fixtures.away_team_goals < fixtures.home_team_goals:
                draws = draws + 1
            else:
                pass

        return draws

    def number_of_goals(self):
        return Goal.objects.filter(team=self.id).count()

    def points(self):
        return self.wins() * 3 + self.draws()


class Fixture(models.Model):

    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team', null=False, blank=False)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team', null=False, blank=False)
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

    goal_id = models.CharField(max_length=100, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, blank=False)
    goal_scorer = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goal_scorer' , null=True, blank=True)
    assist_maker = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='assist_maker', null=True, blank=True)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'Goal: {self.team}, {self.fixture}'

