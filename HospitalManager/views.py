from django.http import HttpRequest
from django.shortcuts import render
from HospitalManager.Models.doctors import DoctorData

User = {
    'name': 'John',
    'age': 20,
    'phone': '0123456789'
}

def demo(request):
    print(DoctorData[0])
    print(request.POST)
    return render(request, 'Home.html', {'user': User})