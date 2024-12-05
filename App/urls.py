from django.urls import path
#-->Importamos las Vistas para las URL
from .views import *

urlpatterns = [
    path('',Home,name='inicio'),
    path('agregar/',Agregar,name='agregar'),
    path('vehiculo/<int:Codigo>/', detalle_vehiculo, name='detalle_vehiculo'),
    path('visualizar/',ver_Vehiculos,name='visualizar'),
    path('modificar/<Codigo>/',Modificar_Vehiculos,name='modificar'),
    path('eliminar/<Codigo>/',Eliminar_Vehiculos,name='eliminar'),
    path('agregar/<int:vehiculo_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar/<int:vehiculo_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('actualizar/<int:vehiculo_id>/<int:cantidad>/', actualizar_carrito, name='actualizar_carrito'),
    
]