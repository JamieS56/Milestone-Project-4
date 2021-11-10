from django import forms
from .models import Team, Fixture
from players.models import Player

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
        widget=forms.TextInput(attrs={'type': 'date', 'min': date.today(), 'class': 'col-6'})
        )
    time = forms.TimeField(
        widget=forms.TextInput(attrs={'type': 'time', 'class': ' col-6'})
    )

    game_played = forms.BooleanField(
        required=False
    )
