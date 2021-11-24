from django.db import models
from teams.models import Team

# Create your models here.


class Player(models.Model):
    """ A Model that represents players at the club. """

    name = models.CharField(max_length=254)
    number = models.IntegerField(null=False)
    position = models.CharField(max_length=15)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, blank=False, related_name='team_players')
    image_url = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )

    def __str__(self):
        return str(self.name)
    
    def appearances(self):
        appearances = 0
        fixtures = self.team.home_team.all() | self.team.away_team.all()
        for fixture in fixtures:
            if fixture.game_played == True:
                appearances += 1

        return appearances

    def clean_sheets(self):
        clean_sheets = 0
        home_fixtures = self.team.home_team.all()
        print(home_fixtures)
        for fixture in home_fixtures:
            if fixture.game_played == True:
                if len(fixture.away_team_goals()) == 0:
                    clean_sheets += 1

        away_fixtures = self.team.away_team.all()
        print(away_fixtures)
        for fixture in away_fixtures:
            if fixture.game_played == True:
                if len(fixture.home_team_goals()) == 0:
                    clean_sheets += 1
        
        print(clean_sheets)
        return clean_sheets
