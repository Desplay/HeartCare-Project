from django.shortcuts import render

User = {
    'name': 'John',
    'age': 20,
    'phone': '0123456789',
}

def demo(request):
    return render(request, 'demo.html', User)