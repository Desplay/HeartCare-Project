from django.urls import re_path
from .WebSockets.Lobby import WSLobby
from .WebSockets.QueueRoom import WSQueueRoom
from .WebSockets.DoctorRoom import WSDoctorRoom


ws_urlpatterns = [
    re_path(r'ws/lobby/', WSLobby.as_asgi()),
    re_path(r'ws/queue-room/', WSQueueRoom.as_asgi()),
    re_path(r'ws/doctor-room/', WSDoctorRoom.as_asgi()),
]
