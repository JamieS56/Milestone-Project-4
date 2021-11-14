from django.contrib import admin
from .models import Team, Fixture, Goal
# Register your models here.
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(Goal)
