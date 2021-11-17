from django.contrib.auth.models import User
from django import forms


class ProfileDataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]

    first_name = forms.CharField(

    )
    last_name = forms.CharField(

    )
    email = forms.EmailField(

    )
