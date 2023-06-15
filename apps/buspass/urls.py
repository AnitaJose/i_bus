"""File for urls in vpn_user."""
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
]
