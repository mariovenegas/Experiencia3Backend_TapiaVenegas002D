from django.shortcuts import render
from .models import Barco

# Create your views here.

def inicio(request):
    return render(request, 'appQuat/inicio.html')

def galeria(request):
    return render(request, 'appQuat/galeria.html')

def barcos(request):
    barcos = Barco.objects.all()
    datos={
        'barcos': barcos
    }
    return render(request, 'appQuat/barcos.html',datos)