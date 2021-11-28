from django import forms
from django.db.models import Q
from teams.models import Team
from players.models import Player

from .models import Fixture, Goal


class FixtureForm(forms.ModelForm):
    """
    Fixture form used on the add fixtures page.
    """

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
    """
    Edit fixture form used on the edit fixtures page.
    """

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
    """
    Add goal form used on the edit fixtures page.
    """

    def __init__(self, *args, **kwargs):

        self.fixture = kwargs.pop('fixture')
        super(AddGoalForm, self).__init__(*args, **kwargs)

        query_set = Player.objects.filter(
            Q(team=self.fixture.home_team) | Q(team=self.fixture.away_team)
            )
        self.fields['goal_scorer'].queryset = query_set
        self.fields['assist_maker'].queryset = query_set

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
        required=True,
        queryset=Player.objects.all()

    )
    assist_maker = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'select form-control'}),
        required=True,
        queryset=Player.objects.all()
    )
