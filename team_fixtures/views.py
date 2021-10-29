from django.shortcuts import render
from .models import Team

# Create your views here.


def teams_page(request):
    ''' A view to return the index page '''
    teams = Team.objects.all()

    context = {
        'teams': teams
    }
    return render(request,'team_fixtures/teams.html', context)
