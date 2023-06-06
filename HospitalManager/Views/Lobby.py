from django.shortcuts import render, redirect

from ..Utils.readData import genderData
from ..Utils.readData import diseaseData
from ..Models.patients import CreatePatient, popPatientLobby

"""
Template get data từ server và render ra html
"""
def LobbyGet(request):
    return render(
        request, "Lobby.html", {"Genders": genderData(), "Diseases": diseaseData()}
    )


"""
Template gửi method thêm bệnh nhân vào hàng đợi của phòng tiếp tân
"""
    
def LobbyPost(request):
    if request.method == "POST":
        CreatePatient(request.POST.dict())
    return redirect("/lobby")

"""
Template gửi method đẩy bệnh nhân ra khỏi phòng tiếp tân để vào phòng chờ
"""
def LobbyPop(request):
    popPatientLobby()
    return redirect("/lobby")