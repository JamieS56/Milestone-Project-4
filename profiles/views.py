from django.shortcuts import render, get_object_or_404
from tickets.models import Ticket
from django.contrib.auth.models import User
from profiles.models  import UserProfile

# Create your views here.


def profile_page(request):
    """ Display the user's profile. """

    profile = request.user

    tickets = Ticket.objects.filter(ticket_holder=profile)
    print(tickets)

    template = 'profiles/profiles.html'
    context = {
        'profile': profile,
        'tickets': tickets,
        'on_profile_page': True
    }

    return render(request, template, context)
