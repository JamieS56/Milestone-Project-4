from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets_page, name='tickets'),


]
