from django.shortcuts import render, redirect, reverse, get_object_or_404
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Team, Fixture
from .forms import FixtureForm


# Create your views here.


def teams_page(request):
    ''' A view to return the index page '''
    teams = Team.objects.all()

    context = {
        'teams': teams
    }
    return render(request,'teams/teams.html', context)


def fixtures_page(request):
    ''' A view to return the index page '''
    fixtures = Fixture.objects.all()
    teams = Team.objects.all()

    for fixture in fixtures:
        fixture.home_team = Team.objects.get(pk=fixture.home_team).name
        fixture.away_team = Team.objects.get(pk=fixture.away_team).name
        print(fixture.time)

    sorted_fixtures = sorted(fixtures, key=lambda fixture: fixture.date)

    context = {
        'fixtures': sorted_fixtures,
        'teams': teams
    }
    return render(request,'teams/fixtures.html', context)


@login_required
def add_fixture(request):
    """ Add a fixture to the fixture list """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FixtureForm(request.POST, request.FILES)
        if request.POST.get("home_team") == request.POST.get('away_team'):
            messages.error(request, "You can't have the same home team and away team.")
            return redirect('add_fixture')
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


def edit_fixture(request, fixture_id):
    """ Edit a fixture """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    fixture = get_object_or_404(Fixture, pk=fixture_id)

    if request.method == 'POST':
        form = EditFixtureForm(request.POST, request.FILES, instance=fixture)
        if request.POST.get("home_team") == request.POST.get('away_team'):
            messages.error(request, "You can't have the same home team and away team.")
            return redirect('add_fixture')
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added fixture!')
            return redirect('fixtures')
        else:
            messages.error(request, 'Failed to add fixture. Please ensure the form is valid.')
    else:
        form = FixtureForm()

    teams = Team.objects.all()
    template = 'teams/edit_fixture.html'
    context = {
        'form': form,
        'teams': teams,
        'fixture': fixture
    }

    return render(request, template, context)
