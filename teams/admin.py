from django.contrib import admin
from .models import Team
# Register your models here.



class FixtureAdmin(admin.ModelAdmin):
    display = ('return_fixture')


# class TeamAdmin(admin.ModelAdmin):
    # readonly_fields('wins', 'draws', 'losses', 'goals_for', 'goals_aganst', 'points')


admin.site.register(Team)

