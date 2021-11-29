from django import forms
from .models import Player

POSITIONS=[
    ('Goalkeeper', 'Goalkeeper'),
    ('Defender', 'Defender'),
    ('Midfield', 'Midfield'),
    ('Forward', "Forward")
]

class PlayerForm(forms.ModelForm):
    """
    This is the form used to edit players.
    """

    class Meta:
        model = Player
        fields = [
            'name',
            'number',
            'position',
            'team'
        ]

    position = forms.CharField(
        widget=forms.Select(
            choices=POSITIONS
        )

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
