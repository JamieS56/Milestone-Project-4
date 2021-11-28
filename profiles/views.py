from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tickets.models import Ticket

from .forms import ProfileDataForm


@login_required
def profile_page(request):
    """ Display the user's profile. """

    # Get all tickets linked with the logged in user.
    profile = request.user
    tickets = Ticket.objects.filter(ticket_holder=profile)[:5]
    form = ProfileDataForm(instance=profile)

    if request.POST:
        form = ProfileDataForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile saved successfully!')

    template = 'profiles/profiles.html'
    context = {
        'profile': profile,
        'tickets': tickets,
        'on_profile_page': True,
        'form': form
    }

    return render(request, template, context)
