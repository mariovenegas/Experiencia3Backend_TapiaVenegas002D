from appQuat.forms import BarcoForm
from django.core.exceptions import RequestAborted
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

def form_barco(request):
    datos={
        'form':BarcoForm()
    }
    if request.method =='POST':
        formulario = BarcoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']='Guardados correctamente'

    return render(request,'appQuat/form_barco.html',datos)


def form_mod_barco(request):
    datos={
        'form':BarcoForm()
    }
    if request.method =='POST':
        formulario = BarcoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']='Guardados correctamente'

    return render(request,'appQuat/form_barco.html',datos)
