from django import forms
from .models import Team, Fixture
from players.models import Player


class FixtureForm(forms.ModelForm):

    class Meta:
        model = Fixture
        fields = '__all__'
    
    all_teams = []

    for teams in Team.objects.all():
        all_teams.append(teams)
        print(teams)
    print(all_teams)

    date_time = forms.DateTimeField(widget=forms.DateTimeInput())
    teams = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple,
        choices=list(Team.objects.values_list('id', 'name'))
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
