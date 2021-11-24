from django.db import models
from django.db.models import Q

# Create your models here.


class Team(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def id(self):
        return self.id

    def get_wins(self):
        wins = 0
        home_fixture_list = self.home_team.all()
        for fixtures in home_fixture_list:
            if fixtures.game_played == True:
                if len(fixtures.home_team_goals()) > len(fixtures.away_team_goals()):
                    wins = wins + 1
                else:
                    pass
            else:
                pass

        away_fixture_list = self.away_team.all()
        for fixtures in away_fixture_list:
            if fixtures.game_played == True:
                if len(fixtures.away_team_goals()) > len(fixtures.home_team_goals()):
                    wins = wins + 1
                else:
                    pass
            else:
                pass
        return wins

    def get_losses(self):
        losses = 0
        home_fixture_list = self.home_team.all()
        for fixtures in home_fixture_list:
            if fixtures.game_played == True:
                if len(fixtures.home_team_goals()) < len(fixtures.away_team_goals()):
                    losses = losses + 1
                else:
                    pass
            else:
                pass

        away_fixture_list = self.away_team.all()
        for fixtures in away_fixture_list:
            if fixtures.game_played == True:
                if len(fixtures.away_team_goals()) < len(fixtures.home_team_goals()):
                    losses = losses + 1
                else:
                    pass
            else:
                pass

        return losses

    def get_draws(self):
        draws = 0
        fixture_list = self.home_team.all() | self.away_team.all()
        for fixtures in fixture_list:
            if fixtures.game_played == True:
                if len(fixtures.home_team_goals()) == len(fixtures.away_team_goals()):
                    draws = draws + 1
                else:
                    pass
            else:
                pass

        
        return draws

    def number_of_goals(self):
        return self.team_goals.count()

    def get_points(self):
        points = self.get_wins() * 3 + self.get_draws()

        return points

    def get_goal_difference(self):
        goals = 0
        home_fixture_list = fixture_list = self.home_team.all()
        for fixtures in fixture_list:
            goals += len(fixtures.home_team_goals()) - len(fixtures.away_team_goals())

        away_fixture_list = fixture_list = self.away_team.all()
        for fixtures in fixture_list:
            goals += len(fixtures.away_team_goals()) - len(fixtures.home_team_goals())


        return goals
        
        


