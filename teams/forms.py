from django import forms
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

    home_team_goals = forms.IntegerField(
        required=False,

        widget=forms.NumberInput(attrs={'min': 0}),
    )
    away_team_goals = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'min': 0}),

    )

    date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'min': date.today()})
        )
    time = forms.TimeField(
        widget=forms.TextInput(attrs={'type': 'time'})
    )

    home_team = forms.ChoiceField(
        required=True,
        widget=forms.Select(),
        choices=list(Team.objects.values_list('id', 'name'))
    )

    away_team = forms.ChoiceField(
        required=True,
        widget=forms.Select(),
        choices=list(Team.objects.values_list('id', 'name'))
    )

    game_played = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False
    )
