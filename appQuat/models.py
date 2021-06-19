from django.db import models

# Create your models here.

#Modelo para el Tipo de Barco

class Tipo_Barco(models.Model):
    idTipoBarco =models.IntegerField(primary_key=True, verbose_name='Id de tipo de barco')
    nombreTipoBarco =models.CharField(max_length=50, verbose_name='Nombre del tipo de barco')

    def __str__(self):
        return self.nombreTipoBarco


#Modelo para el Barco

class Barco(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True, verbose_name='Nombre del barco')
    año = models.CharField(max_length=4, verbose_name='agno')
    descripcion = models.CharField(max_length=20, null=True, blank=True, verbose_name='Descripcion del barco')
    tipo_barco = models.ForeignKey(Tipo_Barco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre