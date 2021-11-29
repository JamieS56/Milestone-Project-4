from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teams.models import Team
from players.models import Player
from helpers import custom_functions
import json

from .models import Fixture, Goal
from .forms import FixtureForm, EditFixtureForm, AddGoalForm


def fixtures_page(request):
    """
    A view to return a table of all the fixtures.
    """

    fixtures = Fixture.objects.all()
    teams = Team.objects.all()

    sorted_fixtures = sorted(fixtures, key=lambda fixture: fixture.date)

    context = {
        'fixtures': sorted_fixtures,
        'teams': teams
    }
    return render(request, 'fixtures/fixtures.html', context)


@login_required
def add_fixture(request):
    """
    Add a fixture to the fixture list
    """

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
            messages.error(
                request,
                'Failed to add fixture. Please ensure the form is valid.'
                )
    else:
        form = FixtureForm()

    teams = Team.objects.all()
    template = 'fixtures/add_fixture.html'
    context = {
        'form': form,
        'teams': teams,

    }

    return render(request, template, context)


@login_required
def edit_fixture(request, fixture_id):
    """
    Edit a fixture on the fixture list.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    fixture = get_object_or_404(Fixture, pk=fixture_id)
    goals = Goal.objects.filter(fixture=fixture)

    if request.method == 'POST':
        form = EditFixtureForm(request.POST, request.FILES, instance=fixture)
        add_goal_form = AddGoalForm(
                            request.POST,
                            request.FILES,
                            fixture=fixture
                            )

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated fixture!')
            return redirect('fixtures')
        else:
            messages.error(
                request,
                'Failed to add fixture. Please ensure the form is valid.'
                )
    else:
        form = EditFixtureForm(instance=fixture)
        add_goal_form = AddGoalForm(
            fixture=fixture,
            initial={'fixture': fixture}
            )

    template = 'fixtures/edit_fixture.html'
    context = {
        'form': form,
        'fixture': fixture,
        'goals': goals,
        'add_goal_form': add_goal_form
    }

    return render(request, template, context)


@login_required
def delete_fixture(request, fixture_id):
    """ Delete a fixture on the fixture list. """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    fixture = get_object_or_404(Fixture, pk=fixture_id)

    fixture.delete()

    messages.success(request, 'Fixture deleted!')

    return redirect('fixtures')


@login_required
def add_goal(request):
    """ This view handles adding goals to the """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    fixture = get_object_or_404(Fixture, pk=request.POST['fixture'])
    add_goal_form = AddGoalForm(request.POST, request.FILES, fixture=fixture)

    if request.method == 'POST':

        team = get_object_or_404(Team, pk=request.POST['team'])

        if add_goal_form.is_valid:
            goal_id = custom_functions.createRandomPK()

            goal_scorer = get_object_or_404(
                            Player,
                            pk=request.POST['goal_scorer']
                            )
            assist_maker = get_object_or_404(
                            Player,
                            pk=request.POST['assist_maker']
                            )
            goal = Goal(
                    goal_id=goal_id,
                    team=team,
                    goal_scorer=goal_scorer,
                    assist_maker=assist_maker,
                    fixture=fixture
                    )
            goal.save()
            messages.success(request, 'Goal has been Saved!')
            return redirect(reverse(
                'edit_fixture',
                kwargs={'fixture_id': fixture.id}
                ))

        else:
            return messages.error(
                request,
                'Sorry, form is invalid please check your form.'
                )


@login_required
def delete_goal(request, goal_id):
    """
    This function deletes individual goals after being deleted on the edit
    fixtures page.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    goal = get_object_or_404(Goal, goal_id=goal_id)

    print(goal)
    fixture = goal.fixture
    goal.delete()
    messages.success(request, 'Successfully deleted goal!')

    return redirect(reverse('edit_fixture', kwargs={'fixture_id': fixture.id}))


@login_required
def delete_team_goals(request):
    """
    This function deletes all goals in relation to the team given
    in the given fixture.It is called when a team is changed in
     a fixture.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    data = json.loads(request.body.decode('utf-8'))
    fixture = get_object_or_404(Fixture, pk=data['fixture'])
    old_team = get_object_or_404(Team, pk=data['old_team'])
    new_team = get_object_or_404(Team, pk=data['new_team'])

    print(f'{fixture}, {old_team}, {new_team}')

    goals = Goal.objects.filter(team=old_team, fixture=fixture)

    goals.delete()

    if fixture.home_team == old_team:
        fixture.home_team = new_team
        fixture.save(update_fields=['home_team'])
        messages.success(request, 'Successfully deleted all home goals!')
    elif fixture.away_team == old_team:
        fixture.away_team = new_team
        fixture.save(update_fields=['away_team'])
        messages.success(request, 'Successfully deleted all away goals!')

    print('redirecting')
    return redirect(reverse('edit_fixture', kwargs={'fixture_id': fixture.id}))
