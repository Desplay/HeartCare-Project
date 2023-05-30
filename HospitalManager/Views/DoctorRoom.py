import json
from django.shortcuts import render, redirect
from ..Models.doctors import findDoctor, parseDoctor, popPatientFromQueue

def DoctorGet(request):
    ID = request.GET.get('ID')
    if(findDoctor(ID) == None):
        return redirect('404')
    return render(request, 'DoctorRoom.html', {'Doctor': parseDoctor(findDoctor(ID))})

def DoctorPost(request):
    ID = request.GET.get('DoctorID')
    print(findDoctor(ID) == None)
    if(findDoctor(ID) == None):
        return redirect('404')
    popPatientFromQueue(findDoctor(ID))
    return  redirect('/doctor?ID=' + ID)