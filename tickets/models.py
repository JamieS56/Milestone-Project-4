from django.db import models

# Create your models here.

from teams.models import Fixture
from profiles.models import UserProfile


class Ticket(models.Model):
    ticket_holder = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    price = 15.00

    def __str__(self):
        return {self.fixture}

    def ticket_date(self):
        return self.fixture.date

    def ticket_time(self):
        return self.fixture.time


class TicketOrder(models.Model):

    order_id = models.CharField(max_length=50, primary_key=True)
    ticket_holder = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField(null=False, blank=False, default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
