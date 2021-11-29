from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from helpers import custom_functions
from .models import Player
from .forms import PlayerForm


def squad(request):
    ''' A view to return a list of all the players. '''
    players = custom_functions.add_no_image(Player.objects.filter(team=1))

    context = {
        'players': players
    }

    return render(request, 'players/squad.html', context)


def player_profile(request, player_id):
    """ A view to show individual players stats """

    player = custom_functions.add_no_image(get_object_or_404(
                                            Player,
                                            pk=player_id
                                            ))

    clean_sheets = player.clean_sheets()
    appearances = player.appearances()

    context = {
        'player': player,
        'clean_sheets': clean_sheets,
        'appearances': appearances
    }

    return render(request, 'players/player_profile.html', context)


@login_required
def edit_player(request, player_id):
    """ A view to edit the individual players stats """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    player = custom_functions.add_no_image(get_object_or_404(
                                            Player,
                                            pk=player_id
                                            ))

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated player!')
            return redirect(reverse('player_profile', args=[player.id]))
        else:
            messages.error(
                request,
                'Failed to update player. Please ensure the form is valid.'
                )
    else:
        form = PlayerForm(instance=player)
        messages.info(request, f'You are editing {player.name}')

    template = 'players/edit_player.html'
    context = {
            'form': form,
            'player': player,
        }

    return render(request, template, context)


@login_required
def add_player(request):
    """
    Add a player
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            messages.success(request, 'Successfully added player!')
            return redirect('players')
        else:
            messages.error(
                request,
                'Failed to add player. Please ensure the form is valid.'
                )
    else:
        form = PlayerForm()

    template = 'players/add_player.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_player(request, player_id):
    """ Delete a player. """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    player = get_object_or_404(Player, pk=player_id)

    player.delete()

    messages.success(request, 'Player deleted!')

    return redirect('players')
