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

    date_time = forms.SplitDateTimeField(label='Split Date Time Field',
                        label_suffix=" : ", required=True,
                        disabled=False, input_date_formats=["%d-%m-%Y"],
                        input_time_formats=["%H:%M"],
                        widget=forms.SplitDateTimeWidget(attrs={'class': 'form-control'}),
                        error_messages={'required': "This field is required."})

    teams = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple,
        choices=list(Team.objects.values_list('id', 'name'))
    )
