from django.shortcuts import render


def Menu(request):
    if request.method == "post":
        pass
    if request.method == "get":
        pass
    return render(request, "Home.html")


def Error404(request, exception):
    return render(request, "404.html")
