from django.shortcuts import render, redirect

from ..Utils.readData import genderData
from ..Utils.readData import diseaseData
from ..Models.patients import CreatePatient, popPatientLobby

def LobbyGet(request):
    return render(
        request, "Lobby.html", {"Genders": genderData(), "Diseases": diseaseData()}
    )

def LobbyPost(request):
    CreatePatient(request.POST.dict())
    return redirect("/lobby")

def LobbyPop(request):
    popPatientLobby()
    return redirect("/lobby")