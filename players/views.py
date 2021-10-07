from django.shortcuts import render
from .models import Player
# Create your views here.


def team(request):
    """ A view to show the whole team."""

    players = Player.objects.all()

    context = {
        'player': players
    }

    return render(request, 'players/team.html', context)

