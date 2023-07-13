import datetime
from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de categoria")


    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="id de producto")
    precio = models.IntegerField( blank=True, verbose_name="Precio")
    stock = models.IntegerField( blank=True, verbose_name="Stock")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    descripcion = models.CharField(max_length=30, blank=True, verbose_name="Nombre producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")


    def __str__(self):
        return self.descripcion
    
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    estado = models.CharField(max_length=20, default='Procesando Pedido')
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)