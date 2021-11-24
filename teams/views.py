from django.shortcuts import render
from .models import Team



# Create your views here.


def table_page(request):
    ''' A view to return the current league table '''

    teams = Team.objects.all()


    for team in teams:
        team.goal_difference = team.get_goal_difference()
        team.points = team.get_points()

    teams = sorted(teams, key=lambda a: a.get_goal_difference(), reverse=True)
    teams = sorted(teams, key=lambda a: a.get_points(), reverse=True)

    context = {
        'teams': teams
    }
    return render(request, 'teams/table.html', context)

