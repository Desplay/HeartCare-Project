from django.shortcuts import render, redirect
from ..Models.doctors import dataRender, addPatientToQueue
from ..Models.patients import PatientsInQueue

"""
Template get data từ server và render ra html
"""
def QueueGet(request):
    return render(request, "QueueRoom.html", {"Doctors": dataRender()})

"""
Template gửi method đẩy bệnh nhân ra khỏi hàng đợi của phòng chờ để và phòng bác sĩ
"""
def QueuePost(request):
    for patient in PatientsInQueue.Return():
        if(addPatientToQueue(patient) == 'Done'):
            PatientsInQueue.remove(patient)
            return redirect("/queue-room")
    return redirect("/queue-room")