from django.shortcuts import render

"""
Hàm render trang chủ
"""
def Menu(request):
    if request.method == "post":
        pass
    if request.method == "get":
        pass
    return render(request, "Home.html")

"""
Hàm render trang lỗi 404
"""
def Error404(request, exception):
    return render(request, "404.html")
