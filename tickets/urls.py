from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets_page, name='tickets'),
    path('checkout/', views.checkout_page, name='checkout'),
    path('checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success_url, name='success'),
    path('cancel/', views.cancel_url, name='cancel'),


]
