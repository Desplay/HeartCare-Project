from django.http import HttpRequest
from django.shortcuts import render

User = {
    'name': 'John',
    'age': 20,
    'phone': '0123456789'
}

def demo(request):
    print(request.POST)
    return render(request, 'Home.html', {'user': User})