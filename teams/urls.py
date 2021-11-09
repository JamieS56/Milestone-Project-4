from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixtures_page, name='fixtures'),
    path('add/', views.add_fixture, name='add_fixture'),
    path('edit/<int:fixture_id>/', views.edit_fixture, name='edit_fixture'),
    path('teams/', views.teams_page, name='teams'),

]
