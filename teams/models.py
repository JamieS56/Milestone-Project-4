from django.db import models

# Create your models here.


class Team(models.Model):
    """
    This model saves the teams name and has methods to find
    the teams wins, losses, draws, points, goals and goal difference.
    """

    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    def get_wins(self):
        wins = 0
        home_fixture_list = self.home_team.all()
        for fixtures in home_fixture_list:
            if fixtures.game_played is True:
                home_goals = fixtures.home_team_goals()
                away_goals = fixtures.away_team_goals()
                if len(home_goals) > len(away_goals):
                    wins = wins + 1
                else:
                    pass
            else:
                pass

        away_fixture_list = self.away_team.all()
        for fixtures in away_fixture_list:
            if fixtures.game_played is True:
                home_goals = fixtures.home_team_goals()
                away_goals = fixtures.away_team_goals()
                if len(away_goals) > len(home_goals):
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
            if fixtures.game_played is True:
                home_goals = fixtures.home_team_goals()
                away_goals = fixtures.away_team_goals()
                if len(away_goals) > len(home_goals):
                    losses = losses + 1
                else:
                    pass
            else:
                pass

        away_fixture_list = self.away_team.all()
        for fixtures in away_fixture_list:
            if fixtures.game_played is True:
                home_goals = fixtures.home_team_goals()
                away_goals = fixtures.away_team_goals()
                if len(home_goals) > len(away_goals):
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
            if fixtures.game_played is True:
                home_goals = fixtures.home_team_goals()
                away_goals = fixtures.away_team_goals()
                if len(home_goals) == len(away_goals):
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
        home_fixture_list = self.home_team.all()
        for fixtures in home_fixture_list:
            home_goals = fixtures.home_team_goals()
            away_goals = fixtures.away_team_goals()
            goals += len(home_goals) - len(away_goals)

        away_fixture_list = self.away_team.all()
        for fixtures in away_fixture_list:
            home_goals = fixtures.home_team_goals()
            away_goals = fixtures.away_team_goals()
            goals += len(away_goals) - len(home_goals)

        return goals
