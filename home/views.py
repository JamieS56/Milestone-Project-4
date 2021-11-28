from datetime import date
from django.shortcuts import render
from helpers import customFunctions
from players.models import Player
from fixtures.models import Fixture


def index(request):
    ''' A view to return the index page '''

    players = customFunctions.add_no_image(
                Player.objects.filter(team=1)
                )
    fixture = Fixture.objects.filter(
                date__gt=date.today()
                ).order_by('date', 'time').first()

    context = {
        'players': players,
        'fixture': fixture
    }

    return render(request, 'home/index.html', context)


def page_not_found(request):

    return render(request, 'home/404.html')
