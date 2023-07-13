from django.urls import path
from .views import * 

urlpatterns=[ 
    path('', p_inicio, name="p_inicio"),
    path('Sobre_Nosotros/',Sobre_Nosotros, name="Sobre_Nosotros"),
    path('Ventas/',Ventas, name="Ventas"),
    path('Adopcion/',Adopcion, name="Adopcion"),
    path('Calculadora/',Calculadora, name="Calculadora"),
    path('crear/', crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    #
    path('tienda/',tienda, name="tienda"),
    path('tienda/',tienda, name="tienda"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]   