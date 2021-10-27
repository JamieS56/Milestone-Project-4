from django.shortcuts import render
from players.models import Player
# Create your views here.


def add_no_image(players):

    try:
        for player in players:
            if player.image_url == '':
                player.image_url = 'no-image.jpg'
    except TypeError:
        if players.image_url == '':
            players.image_url = 'no-image.jpg'

    return players


def index(request):
    ''' A view to return the index page '''

    players = add_no_image(Player.objects.all())

    context = {
        'players': players
    }

    return render(request, 'home/index.html', context)
