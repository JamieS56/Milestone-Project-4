from django import forms
from django.db import models
from .models import Team, Fixture
from players.models import Player

from datetime import date

class FixtureForm(forms.ModelForm):

    class Meta:
        model = Fixture
        fields = '__all__'

    all_teams = []

    for teams in Team.objects.all():
        all_teams.append(teams)
        print(teams)

    home_team_goals = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 0})
    )
    away_team_goals = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 0})
    )

    date_time = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date', 'min':date.today()}, time_attrs={'type': 'time'})
        )

    home_team = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select(),
        choices=list(Team.objects.values_list('id', 'name'))
    )

    away_team = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select(),
        choices=list(Team.objects.values_list('id', 'name'))
    )
