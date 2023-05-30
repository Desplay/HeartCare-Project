import json
from django.shortcuts import render, redirect
from ..Models.doctors import dataRender, addPatientToQueue
from ..Models.patients import PatientsInQueue

def QueueGet(request):
    return render(request, "QueueRoom.html", {"Doctors": dataRender()})


def QueuePost(request):
    for patient in PatientsInQueue.Return():
        if(addPatientToQueue(patient) == 'Done'):
            PatientsInQueue.remove(patient)
            return redirect("/queue-room")
    return redirect("/queue-room")