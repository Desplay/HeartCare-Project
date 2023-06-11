import json
from django.shortcuts import render, redirect
from ..Models.doctors import findDoctor, parseDoctor, popPatientFromQueue


"""
Hàm render trang bác sĩ
"""
def DoctorGet(request):
    ID = request.GET.get('ID')
    if(findDoctor(ID) == None):
        return redirect('404')
    return render(request, 'DoctorRoom.html', {'Doctor': parseDoctor(findDoctor(ID))})


"""
Hàm đẩy bệnh nhân ra khỏi hàng đợi của phòng bác sĩ
"""
def DoctorPost(request):
    ID = request.GET.get('DoctorID')
    if(findDoctor(ID) == None):
        return redirect('404')
    popPatientFromQueue(findDoctor(ID))
    return  redirect('/doctor?ID=' + ID)