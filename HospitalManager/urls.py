from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.test, name='test'),
]
