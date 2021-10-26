from django.urls import path
from . import views

urlpatterns = [
    path('', views.squad, name='players'),
    path('<int:player_id>/', views.player_profile, name='player_profile'),
    path('edit/<int:player_id>/', views.edit_player, name='edit_player'),
]
