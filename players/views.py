from django.shortcuts import render, get_object_or_404
from .models import Player
# Create your views here.


def team(request):
    ''' A view to return the index page '''

    players = Player.objects.all()
    for player in players:
        if player.close_up_image_url == '':
            print(player.close_up_image_url)
            player.close_up_image_url = 'media/no-image.jpg'
            print(player.close_up_image_url)

    context = {
        'players': players
    }

    return render(request, 'players/teams.html', context)


def player_profile(request, player_id):
    """ A view to show individual players stats """

    player = get_object_or_404(Player, pk=player_id)

    context = {
        'player': player,
    }

    return render(request, 'players/player_profile.html', context)
