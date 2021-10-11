from django.shortcuts import render
from .models import Player
# Create your views here.


def team(request):
    ''' A view to return the index page '''

    players = Player.objects.all()

    context = {
        'players': players
    }

    return render(request, 'players/teams.html', context)
