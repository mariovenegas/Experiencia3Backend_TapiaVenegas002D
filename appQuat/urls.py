from django.urls import path
from .views import inicio, galeria, barcos

urlpatterns =[
    path('',inicio,name="inicio"),
    path('galeria',galeria,name="galeria"),
    path('barcos', barcos, name="barcos"),
]