from django.shortcuts import render
from .models import Team

# Create your views here.

 
def table_page(request):
    ''' A view to return the current league table '''

    teams = Team.objects.all()

    teams = sorted(teams, key=lambda a: a.get_goal_difference(), reverse=True)
    teams = sorted(teams, key=lambda a: a.get_points(), reverse=True)

    for team in teams:
        fixture_list = team.home_team.all() | team.away_team.all()
        print(f'{team} {team.get_points()} {len(fixture_list)}')

    context = {
        'teams': teams
    }
    return render(request, 'teams/table.html', context)
