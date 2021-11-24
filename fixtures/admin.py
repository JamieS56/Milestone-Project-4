from django.contrib import admin
from .models import Fixture, Goal
# Register your models here.


class FixtureAdmin(admin.ModelAdmin):
    display = ('return_fixture')


admin.site.register(Fixture, FixtureAdmin)
admin.site.register(Goal)
