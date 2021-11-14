from django.db import models
from django import forms
from django.shortcuts import get_object_or_404
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


class Fixture(models.Model):

    HOME_OR_AWAY = [
        ('H', 'Home'),
        ('A', 'Away')
    ]

    home_or_away = models.CharField(max_length=1, choices=HOME_OR_AWAY)
    opposition_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    messi_ankles_team_goals = models.IntegerField(null=True, blank=True)
    opposition_team_goals = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    game_played = models.BooleanField(default=False)


class Goal(models.Model):

    goal_id = models.CharField(max_length=100, primary_key=True)
    goal_scorer = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goal_scorer' , null=True, blank=True)
    assist_maker = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='assist_maker', null=True, blank=True)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)

    @classmethod
    def create(cls, goal_id, goal_scorer, assist_maker, fixture):
        goal = cls(goal_id=goal_id, goal_scorer=goal_scorer, assist_maker=assist_maker, fixture=fixture)
        return goal


class GoalManager(models.Model):

    def create_goal(self, goal_id, goal_scorer, assist_maker, fixture):
        goal = self.create(goal_id=goal_id, goal_scorer=goal_scorer, assist_maker=assist_maker, fixture=fixture)

        objects = GoalManager()
