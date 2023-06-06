from django.shortcuts import render, redirect

from ..Utils.readData import genderData
from ..Utils.readData import diseaseData
from ..Models.patients import findPatient, CreatePatient, removePatientWithID

"""
Hàm render trang chỉnh sửa bệnh nhân
"""
def EditPatientGet(request):
    IDCode = request.GET.get("ID")
    return render(
        request,
        "EditPatient.html",
        {
            "patient":findPatient(IDCode),
            "Genders": genderData(),
            "Diseases": diseaseData(),
        },
    )


"""
Hàm chỉnh sửa bệnh nhân
"""
def EditPatientPost(request):
    removePatientWithID(request.POST.dict()['IDCode'])
    CreatePatient(request.POST.dict())
    return redirect("/lobby")