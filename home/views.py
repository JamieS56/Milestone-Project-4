from django.shortcuts import render
from customFunctions import customFunctions
from players.models import Player


def index(request):
    ''' A view to return the index page '''

    players = customFunctions.add_no_image(Player.objects.all())

    context = {
        'players': players
    }

    return render(request, 'home/index.html', context)
