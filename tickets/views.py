from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import TicketOrderForm, CheckoutForm
from .models import Ticket
from teams.models import Fixture
from django.conf import settings
import stripe

# Create your views here.


def tickets_page(request):

    form = TicketOrderForm(request.POST, request.FILES)
    context = {
        'form': form
    }
    return render(request, 'tickets/tickets.html', context)


def checkout_page(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    fixture = Fixture.objects.filter(pk=request.POST['fixture'])
    grand_total = int(request.POST['number_of_tickets']) * 15
    order_details = {
        'ticket_holder': request.user,
        'fixture': fixture[0],
        'number_of_tickets': request.POST['number_of_tickets'],
        'grand_total': grand_total
    }

    checkout_form = CheckoutForm()


    if request.method == 'POST':
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

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
            amount=(order_details['grand_total']* 100),
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)

    context = {
        'form': checkout_form,
        'order_details': order_details,
        'stripe_public_key': stripe_public_key,
        'stripe_secret_key': stripe_secret_key,
        'client_secret': 'test client secret'
    }

    return render(request, 'tickets/checkout.html', context)

def create_checkout_session():
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_bag
    total
    stripe_total
    stripe.api_key = stripe_secret_key

    stripe.PaymentIntent.create(

    )



def success_url(request):

    return render(request, 'tickets/success.html', context)


def cancel_url(request):

    return render(request, 'tickets/cancel.html', context)

