from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    """ This is the form used to edit players. """

    class Meta:
        model = Player
        fields = [
            'name',
            'number',
            'position',
            'team'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
