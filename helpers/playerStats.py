from teams.models import Team
from fixtures.models import Fixture, Goal
from players.models import Player
from django.shortcuts import get_object_or_404
from django.db.models import Q


def goals(player):
    goals = Goal.objects.filter(goal_scorer=player)
    return goals


def assists(player):
    assists = Goal.objects.filter(assist_maker=player)
    return assists


def clean_sheets():
    messi_ankles = get_object_or_404(Team, pk=1)
    home_fixtures = Fixture.objects.filter(home_team=messi_ankles)
    away_fixtures = Fixture.objects.filter(away_team=messi_ankles)
    clean_sheets = 0

    print(home_fixtures)

    for fixture in home_fixtures:
        print(fixture.away_team_goals())
        if len(fixture.away_team_goals()) == 0:
            clean_sheets += 1
            print(clean_sheets)

    for fixture in away_fixtures:
        if len(fixture.home_team_goals()) == 0:
            clean_sheets += 1
            print(clean_sheets)

    print(f'final: {clean_sheets}')
    return clean_sheets


def appearances():
    messi_ankles = get_object_or_404(Team, pk=1)
    appearances = Fixture.objects.filter(Q(home_team=messi_ankles) & Q(game_played=True) | Q(away_team=messi_ankles) & Q(game_played=True))
    return appearances
