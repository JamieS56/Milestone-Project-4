from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Team, Fixture, Goal
from players.models import Player
from .forms import FixtureForm, EditFixtureForm, AddGoalForm
from customFunctions import customFunctions
import json

# Create your views here.


def fixtures_page(request):
    ''' A view to return a table of all the fixtures. '''

    fixtures = Fixture.objects.all()
    teams = Team.objects.all()

    sorted_fixtures = sorted(fixtures, key=lambda fixture: fixture.date)

    context = {
        'fixtures': sorted_fixtures,
        'teams': teams
    }
    return render(request, 'teams/fixtures.html', context)


def table_page(request):
    ''' A view to return the current league table '''

    teams = Team.objects.all()
    sorted_teams = sorted(teams, key=lambda team: team.points(), reverse=True)
    context = {
        'teams': sorted_teams
    }
    return render(request, 'teams/table.html', context)



@login_required
def add_fixture(request):
    """ Add a fixture to the fixture list """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FixtureForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            messages.success(request, 'Successfully added fixture!')
            return redirect('fixtures')
        else:
            messages.error(request, 'Failed to add fixture. Please ensure the form is valid.')
    else:
        form = FixtureForm()

    teams = Team.objects.all()
    template = 'teams/add_fixture.html'
    context = {
        'form': form,
        'teams': teams,
    }

    return render(request, template, context)


@login_required
def edit_fixture(request, fixture_id):
    """ Edit a fixture on the fixture list. """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    fixture = get_object_or_404(Fixture, pk=fixture_id)
    goals = Goal.objects.filter(fixture=fixture)

    if request.method == 'POST':
        form = EditFixtureForm(request.POST, request.FILES, instance=fixture)
        add_goal_form = AddGoalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added fixture!')
            return redirect('fixtures')
        else:
            messages.error(request, 'Failed to add fixture. Please ensure the form is valid.')
    else:
        form = EditFixtureForm(instance=fixture)
        add_goal_form = AddGoalForm(initial={'fixture': fixture})

    teams = Team.objects.all()
    players = Player.objects.all()
    template = 'teams/edit_fixture.html'
    context = {
        'form': form,
        'teams': teams,
        'fixture': fixture,
        'goals': goals,
        'players': players,
        'add_goal_form': add_goal_form

    }

    return render(request, template, context)


def add_goals(goals_list):
    """ This view handles adding goals to the """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':

    for goals in goals_list:
        try:
            if goals['team'] == '1':

                fixture = get_object_or_404(Fixture, pk=goals['fixture'])
                team = get_object_or_404(Team, pk=goals['team'])
                goal_scorer = get_object_or_404(Player, pk=goals['goal_scorer'])
                assist_maker = get_object_or_404(Player, pk=goals['assist_maker'])
                goal = Goal(goal_id=goals['goal_id'], team=team, goal_scorer=goal_scorer, assist_maker=assist_maker, fixture=fixture)
                goal.save()
                return 'success'
            else:
                fixture = get_object_or_404(Fixture, pk=goals['fixture'])
                team = get_object_or_404(Team, pk=goals['team'])
                goal = Goal(goal_id=goals['goal_id'], team=team, goal_scorer=None, assist_maker=None, fixture=fixture)
                goal.save()
                return 'success'

        except AttributeError:
            return 'error'
    



GOAL_LIST = []


@login_required
def handle_goal(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    try:

        goal_data = json.loads(request.body.decode('utf-8'))
        print(goal_data)

    except AttributeError:
        pass

    if goal_data['submit'] == 'True':
        goals_list = GOAL_LIST
        goal_success = add_goals(goals_list)
        if goal_success == 'success':
            messages.success(request, 'Successfully added Goal!')
        else:
            messages.error(request, 'Failed to add goal. Please ensure the form is valid.')


        return JsonResponse({'submit': 'success'})

    if goal_data['add_or_remove'] == 'add':
        goal_data['goal_id'] = customFunctions.createRandomPK()
        GOAL_LIST.append(goal_data)

        return JsonResponse(goal_data)

    if goal_data['add_or_remove'] == 'remove':
        for goal in range(len(GOAL_LIST)):
            if GOAL_LIST[goal]['goal_id'] == goal_data['goal_id']:
                del GOAL_LIST[goal]
                break

        return JsonResponse({'game_id': '0'})
