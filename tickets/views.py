from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
import stripe
from fixtures.models import Fixture
from helpers import custom_functions

from .forms import TicketOrderForm, CheckoutForm
from .models import Ticket


def tickets_page(request):
    '''A view to display the initial page of the purchasing tickets method.'''

    form = TicketOrderForm(request.POST, request.FILES)
    context = {
        'form': form
    }
    return render(request, 'tickets/tickets.html', context)


def checkout_page(request):
    '''
    A view for the checkout page where the user
    inputs there card info and purchasing details.
    '''

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    grand_total = int(request.POST.get('number_of_tickets', False)) * 15
    fixture = Fixture.objects.filter(pk=request.POST['fixture'])

    order_details = {
            'fixture': request.POST['fixture'],
            'number_of_tickets': request.POST.get('number_of_tickets', False),
            'grand_total': grand_total
        }

    request.session['order_details'] = order_details

    # Prefilling the checkout form if user data is saved.
    if request.user.is_authenticated:
        try:
            profile = User.objects.get(username=request.user)
            checkout_form = CheckoutForm(initial={
               'first_name': profile.first_name,
               'last_name': profile.last_name,
               'email': profile.email,
            })
        except User.DoesNotExist:
            checkout_form = CheckoutForm
    else:
        checkout_form = CheckoutForm

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=(grand_total * 100),
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'form': checkout_form,
        'order_details': order_details,
        'fixture': fixture[0],
        'stripe_public_key': stripe_public_key,
        'stripe_secret_key': stripe_secret_key,
        'client_secret': intent.client_secret
    }

    return render(request, 'tickets/checkout.html', context)


def handle_checkout(request):
    ''''A function that handles the data from a ticket purchase. '''

    if request.method == 'POST':

        order_details = request.session['order_details']

        fixture = Fixture.objects.filter(pk=order_details['fixture'])
        order_details['fixture'] = fixture[0]

        form_data = {
            'first_name': request.POST.get('first_name', False),
            'last_name': request.POST.get('last_name', False),
            'email': request.POST.get('email', False),
        }

        checkout_form = CheckoutForm(form_data)
        ticket_id = str(custom_functions.createRandomPK())
        full_name = form_data['first_name']+' '+form_data['last_name']

        if checkout_form.is_valid():

            # Adding the available info to the ticket object.
            if request.user.is_authenticated:
                user = request.user
                ticket = Ticket(
                    ticket_id=ticket_id,
                    ticket_holder=user,
                    fixture=order_details['fixture'],
                    number_of_tickets=order_details['number_of_tickets'],
                    price=order_details['grand_total'],
                    full_name=full_name,
                    email=form_data['email']
                    )
                ticket.save()
                request.session['order_details'] = {}
                email_message = (
                    f'Hello {full_name},\n\n'
                    f'Your tickets for {str(ticket.fixture)} are confirmed.'
                    f'\nTotal: ${ticket.price}.\n\n'
                    f'We hope you enjoy the game!\n The Messi Ankles Team'
                    )
                send_mail(
                    f'Booking Confirmation <{ticket.ticket_id}>',
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [ticket.email],
                    fail_silently=False
                )

                return redirect('success', ticket_id=ticket.ticket_id)
            else:
                ticket = Ticket(
                    ticket_id=ticket_id,
                    ticket_holder=None,
                    fixture=order_details['fixture'],
                    number_of_tickets=order_details['number_of_tickets'],
                    price=order_details['grand_total'],
                    full_name=full_name,
                    email=form_data['email']
                    )
                ticket.save()
                request.session['order_details'] = {}
                return redirect('success', ticket=ticket.ticket_id)

        else:
            messages.error(request, 'There was an error with your card. \
                Please double check your information.')
            return redirect(reverse('checkout'))


def success_url(request, ticket_id):
    ''' Succesful purchase page.'''
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if not ticket:
        messages.error(request, 'Checkout error, there is no ticket.')
        return redirect('home')

    context = {
        'ticket': ticket
    }

    return render(request, 'tickets/success.html', context)


def cancel_url(request):
    ''' Canceled purchase page.'''

    return render(request, 'tickets/cancel.html')
