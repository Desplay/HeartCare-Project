from django.http import HttpRequest
from django.shortcuts import render

from .Models.doctors import dataRender
from .Utils.readData import genderData
from .Utils.readData import diseaseData

User = {"name": "John", "age": 20, "phone": "0123456789"}


def Menu(request):
    return render(request, "Home.html")


def LobbyGet(request):
    return render(request, "Lobby.html", {"Genders": genderData(), "Diseases": diseaseData()})


def LobbyPost(request):
    
    return render(request, "Lobby.html", {"Genders": genderData(), "Diseases": diseaseData()})
# print(dataRender()[0]["Doctor"].name)
# print(request.POST)
