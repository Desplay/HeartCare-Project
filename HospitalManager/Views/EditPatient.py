from django.shortcuts import render, redirect

from ..Utils.readData import genderData
from ..Utils.readData import diseaseData
from ..Models.patients import findPatient, CreatePatient, removePatientWithID


def EditPatientGet(request):
    IDCode = request.GET.get("ID")
    return render(
        request,
        "EditPatient.html",
        {
            "patient": findPatient(IDCode),
            "Genders": genderData(),
            "Diseases": diseaseData(),
        },
    )

def EditPatientPost(request):
    removePatientWithID(request.POST.dict()['IDCode'])
    CreatePatient(request.POST.dict())
    return redirect("/lobby")