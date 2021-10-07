from django.shortcuts import render
from players.models import Player
# Create your views here.


def index(request):
    ''' A view to return the index page '''

    players = Player.objects.all()

    context = {
        'player': players
    }

    return render(request, 'home/index.html', context)
