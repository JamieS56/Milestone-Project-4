from django.shortcuts import render, get_object_or_404
from tickets.models import Ticket
from django.contrib.auth.models import User


def profile_page(request):
    """ Display the user's profile. """

    # Get all tickets linked with the logged in user.
    profile = request.user
    tickets = Ticket.objects.filter(ticket_holder=profile)

    template = 'profiles/profiles.html'
    context = {
        'profile': profile,
        'tickets': tickets,
        'on_profile_page': True
    }

    return render(request, template, context)
