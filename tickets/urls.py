from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets_page, name='tickets'),
    path('checkout/', views.checkout_page, name='checkout'),
    path('handle_checkout/', views.handle_checkout, name='handle_checkout'),
    path('success/<int:ticket_id>/', views.success_url, name='success'),
    path('cancel/', views.cancel_url, name='cancel'),

]
