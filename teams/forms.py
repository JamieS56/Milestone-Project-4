from django import forms
from .models import Team, Fixture, Goal
from players.models import Player
from customFunctions import customFunctions

from datetime import date


class FixtureForm(forms.ModelForm):

    class Meta:
        model = Fixture
        fields = '__all__'

    home_or_away = forms.ChoiceField(
        required=True,
        widget=forms.Select(),
        choices=[
            ('H', 'Home'),
            ('A', 'Away')
        ]
    )
    opposition_team = forms.ChoiceField(
        required=True,
        widget=forms.Select(),
        choices=Team.objects.values_list('id', 'name').exclude(name='Messi Ankles'),
    )
    messi_ankles_team_goals = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'min': 0}),
    )
    opposition_team_goals = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'min': 0}),
    )
    date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'min': date.today()})
        )
    time = forms.TimeField(
        widget=forms.TextInput(attrs={'type': 'time'})
    )
    game_played = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False
    )


class EditFixtureForm(forms.ModelForm):

    class Meta:
        model = Fixture
        fields = '__all__'

    home_team = forms.ModelChoiceField(
        required=True,
        queryset=Team.objects.all()
    )
    opposition_team = forms.ModelChoiceField(
        required=True,
        queryset=Team.objects.all()
    )
    home_team_goals = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'min': 0}),
    )
    away_team_goals = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'min': 0}),
    )
    date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'col-6'})
        )
    time = forms.TimeField(
        widget=forms.TextInput(attrs={'type': 'time', 'class': ' col-6'})
    )

    game_played = forms.BooleanField(
        required=False
    )


class AddGoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = '__all__'

    fixture = forms.ModelChoiceField(
        widget=forms.HiddenInput(),
        queryset=Fixture.objects.all()
    )

    team = forms.ModelChoiceField(
        widget=forms.HiddenInput(attrs={'id': 'goal_home_team'}),
        queryset=Team.objects.all()
    )

    goal_id = forms.IntegerField(
        widget=forms.HiddenInput(attrs={'value':customFunctions.createRandomPK})
        )
    goal_scorer = forms.ModelChoiceField(
        queryset=Player.objects.all()
    )
    assist_maker = forms.ModelChoiceField(
        queryset=Player.objects.all()
    )
    fixture = forms.IntegerField(
        widget=forms.HiddenInput(attrs={'value': '{{ fixture }}'})
    )
