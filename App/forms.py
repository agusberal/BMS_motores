#--->Importamos 'FORMS'
from django import forms
#---> Importamos los Modelos/Tablas
from .models import *

class NuevoVehiculos(forms.ModelForm):
    class Meta:
        model=Vehiculos
        fields='__all__'