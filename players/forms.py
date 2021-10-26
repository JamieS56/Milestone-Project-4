from django import forms
from .widgets import CustomClearableFileInput
from .models import Player


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
