from datetime import date
from django import forms
from django.contrib.auth.models import User
from fixtures.models import Fixture

from .models import TicketOrder


class TicketOrderForm(forms.ModelForm):
    """
    The form used to select what game the tickets are for
    and how many are wanted.
    """

    class Meta:
        model = TicketOrder
        fields = [
            'fixture',
            'number_of_tickets'
        ]

    fixture = forms.ModelChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
        queryset=Fixture.objects.filter(
                    date__gt=date.today()
                    ).order_by('date', 'time')

    )
    number_of_tickets = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
                attrs={'min': 1, 'class': 'col-6 form-control'}
                ),
        initial=1
    )


class CheckoutForm(forms.ModelForm):
    """ The form used on the checkout for inputing the user information"""

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]

    first_name = forms.CharField(
        required=True
    )
    last_name = forms.CharField(
        required=True
    )
    email = forms.EmailField(
        required=True
    )
