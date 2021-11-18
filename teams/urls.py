from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixtures_page, name='fixtures'),
    path('add/', views.add_fixture, name='add_fixture'),
    path('edit/<int:fixture_id>/', views.edit_fixture, name='edit_fixture'),
    path('handle_goal/', views.handle_goal, name='handle_goal'),
    path('add_goal/', views.add_goal, name='add_goal'),
    path('delete_goal/<int:goal_id>/', views.delete_goal, name='delete_goal'),
    path('table/', views.table_page, name='table'),

]
