from django.shortcuts import render, get_object_or_404
from .models import Player
# Create your views here.


def add_no_image(players):

    try:
        for player in players:
            if player.close_up_image_url == '':
                player.close_up_image_url = 'no-image.jpg'
    except TypeError:
        if players.close_up_image_url == '':
            players.close_up_image_url = 'no-image.jpg'

    return players


def squad(request):
    ''' A view to return the index page '''
    players = add_no_image(Player.objects.all())

    context = {
        'players': players
    }

    return render(request, 'players/squad.html', context)


def player_profile(request, player_id):
    """ A view to show individual players stats """

    player = add_no_image(get_object_or_404(Player, pk=player_id))

    context = {
        'player': player,
    }

    return render(request, 'players/player_profile.html', context)
