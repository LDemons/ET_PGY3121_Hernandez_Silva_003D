from django.contrib import admin
from .models import Categoria, Producto,detalle_boleta,Boleta


admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)