from django.urls import re_path
from .customer import WSLobby

ws_urlpatterns = [
    re_path(r'ws/lobby/', WSLobby.as_asgi())
]
