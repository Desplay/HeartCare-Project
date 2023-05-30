from django.urls import path

from .Views.views import Menu, Error404
from .Views.Lobby import LobbyGet, LobbyPost, LobbyPop
from .Views.EditPatient import EditPatientGet, EditPatientPost
from .Views.QueueRoom import QueueGet, QueuePost

urlpatterns = [
    path("", Menu, name="Menu"),
    path("lobby/", LobbyGet, name="LobbyGet"),
    path("lobby/submit", LobbyPost, name="LobbyPost"),
    path("lobby/pop", LobbyPop, name="LobbyPop"),
    path("edit-patient", EditPatientGet, name="editPatientGet"),  # type: ignore
    path("edit-patient/submit", EditPatientPost, name="editPatientPost"), # type: ignore
    path("queue-room/", QueueGet, name="QueueGet"),
    path("queue-room/move", QueuePost, name="QueuePop") # type: ignore
]

handler404 = Error404
