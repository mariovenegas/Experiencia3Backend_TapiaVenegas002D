from django import forms
from django.forms import ModelForm
from .models import Barco

class BarcoForm(ModelForm):
    class Meta:
        model= Barco
        fields =['nombre','año','descripcion','tipo_barco']