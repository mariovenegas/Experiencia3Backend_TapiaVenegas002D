from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'appQuat/inicio.html')

def galeria(request):
    return render(request, 'appQuat/galeria.html')