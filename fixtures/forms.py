from django import forms
from .models import Fixture, Goal
from teams.models import Team
from players.models import Player
from helpers import customFunctions

from datetime import date


class FixtureForm(forms.ModelForm):

    class Meta:
        model = Fixture
        fields = [
            'home_team',
            'away_team',
            'date',
            'time',
            'game_played'
        ]

    home_team = forms.ModelChoiceField(
        required=True,
        queryset=Team.objects.all()
    )
    away_team = forms.ModelChoiceField(
        required=True,
        queryset=Team.objects.all()
    )
    date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'col-6'})
        )
    time = forms.TimeField(
        widget=forms.TextInput(attrs={'type': 'time', 'class': 'col-6'})
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
        widget=forms.Select(attrs={'class': 'team-select'}),
        queryset=Team.objects.all()
    )
    away_team = forms.ModelChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'team-select'}),
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
        widget=forms.CheckboxInput(),
        required=False

    )


class AddGoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = '__all__'

    fixture = forms.ModelChoiceField(
        required=True,
        widget=forms.HiddenInput(),
        queryset=Fixture.objects.all()
    )

    team = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'select form-control'})
    )

    goal_id = forms.IntegerField(
        widget=forms.HiddenInput(attrs={})
        )
    goal_scorer = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'select form-control', }),
        required=False,
        queryset=Player.objects.all()
    )
    assist_maker = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'select form-control'}),
        required=False,
        queryset=Player.objects.all()
    )

