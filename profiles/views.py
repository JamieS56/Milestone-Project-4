from django.shortcuts import render, get_object_or_404
from tickets.models import Ticket
from django.contrib.auth.models import User
from .forms import ProfileDataForm


def profile_page(request):
    """ Display the user's profile. """

    # Get all tickets linked with the logged in user.
    profile = request.user
    tickets = Ticket.objects.filter(ticket_holder=profile)
    form = ProfileDataForm(instance=profile)

    if request.POST:
        form = ProfileDataForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    template = 'profiles/profiles.html'
    context = {
        'profile': profile,
        'tickets': tickets,
        'on_profile_page': True,
        'form': form
    }

    return render(request, template, context)
