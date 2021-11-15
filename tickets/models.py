from django.db import models

# Create your models here.

from teams.models import Fixture
from profiles.models import UserProfile

class Ticket(models.Model):
    ticket_holder = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def __str__(self):
        return {self.fixture}

    def ticket_date(self):
        return self.fixture.date

    def ticket_time(self):
        return self.fixture.time