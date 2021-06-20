from django.urls import path
from .views import inicio, galeria, barcos, form_barco, form_mod_barco, form_del_barco

urlpatterns =[
    path('',inicio,name="inicio"),
    path('galeria',galeria,name="galeria"),
    path('barcos', barcos, name="barcos"),
    path('form-barco',form_barco,name="form_barco"),
    path('form-mod-barco/<id>', form_mod_barco, name="form_mod_barco"),
    path('form-del-barco/<id>', form_del_barco, name="form_del_barco")

]