from django.db import models


# Create your models here.

from teams.models import Fixture
from django.contrib.auth.models import User


class Ticket(models.Model):
    ticket_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField(null=False, blank=False, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def __str__(self):
        return f'{self.ticket_holder} {self.fixture} x{self.number_of_tickets}'

    def ticket_date(self):
        return self.fixture.date

    def ticket_time(self):
        return self.fixture.time


class TicketOrder(models.Model):

    order_id = models.CharField(max_length=50, primary_key=True)
    ticket_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField(null=False, blank=False, default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
