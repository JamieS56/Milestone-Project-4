from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.fixtures_page,
        name='fixtures'
        ),
    path(
        'add/',
        views.add_fixture,
        name='add_fixture'
          ),
    path(
        'edit/<int:fixture_id>/',
        views.edit_fixture,
        name='edit_fixture'
        ),
    path(
        'delete_fixture/<int:fixture_id>/',
        views.delete_fixture,
        name='delete_fixture'
        ),
    path(
        'add_goal/',
        views.add_goal,
        name='add_goal'
        ),
    path(
        'delete_goal/<int:goal_id>/',
        views.delete_goal,
        name='delete_goal'
        ),
    path(
        'delete_team_goals/',
        views.delete_team_goals,
        name='delete_team_goals'
        ),
]
