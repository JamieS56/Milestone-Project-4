from django.contrib import admin
from .models import TicketOrder, Ticket

# Register your models here.

admin.site.register(Ticket)
admin.site.register(TicketOrder)
