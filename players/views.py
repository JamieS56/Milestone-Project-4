from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customFunctions import customFunctions
from .models import Player
from .forms import PlayerForm




def squad(request):
    ''' A view to return a list of all the players. '''
    players = customFunctions.add_no_image(Player.objects.all())

    context = {
        'players': players
    }

    return render(request, 'players/squad.html', context)


def player_profile(request, player_id):
    """ A view to show individual players stats """

    player = customFunctions.add_no_image(get_object_or_404(Player, pk=player_id))

    context = {
        'player': player,
    }

    return render(request, 'players/player_profile.html', context)


@login_required
def edit_player(request, player_id):
    """ A view to edit the individual players stats """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    player = customFunctions.add_no_image(get_object_or_404(Player, pk=player_id))

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated player!')
            return redirect(reverse('player_profile', args=[player.id]))
        else:
            messages.error(request, 'Failed to update player. Please ensure the form is valid.')
    else:
        form = PlayerForm(instance=player)
        messages.info(request, f'You are editing {player.name}')

    template = 'players/edit_player.html'
    context = {
            'form': form,
            'player': player,
        }

    return render(request, template, context)
