from django.urls import path
from . import views

urlpatterns = [
    path('', views.Menu, name='Menu'),
    path('lobby/', views.LobbyGet, name='Lobby'),
    path('lobby/submit/', views.LobbyPost, name='LobbyPost'),
]
