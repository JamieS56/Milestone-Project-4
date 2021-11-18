from django import forms
from .widgets import CustomClearableFileInput
from .models import Player


class PlayerForm(forms.ModelForm):
    """ This is the form used to edit players. """

    class Meta:
        model = Player
        fields = '__all__'

    image_url = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput()
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
