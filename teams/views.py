from django.shortcuts import render, redirect, reverse, get_object_or_404
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

    context = {
        'fixtures': fixtures,
        'teams': teams
    }
    return render(request,'teams/fixtures.html', context)


@login_required
def add_fixture(request):
    """ Add a product to the store """
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
