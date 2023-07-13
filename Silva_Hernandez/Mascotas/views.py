from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm,RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from Mascotas.compra import Carrito
from django.db.models import F

# Create your views here.
def p_inicio(request):
    return render(request, 'p_inicio.html')

def Sobre_Nosotros(request):
    return render(request, 'Sobre_Nosotros.html')


@login_required
def Ventas(request):
    productos = Producto.objects.all()
    datos = {'productis': productos}
    return render(request, 'Ventas.html', datos)


def Adopcion(request):
    return render(request, 'Adopcion.html')

def Calculadora(request):
    return render(request, 'Calculadora.html')

def registrar(request):
    data = {
        'form' : RegistroUserForm()         
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data = request.POST)  
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],
                  password=formulario.cleaned_data["password1"])
            login(request,user)   
            return redirect('p_inicio')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

@login_required
def crear(request):
    if request.method == "POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()  # similar al insert de sql en función
            return redirect('ventas')
    else:
        productoform = ProductoForm()
    return render(request, 'Crear.html', {'producto_form': productoform})

@login_required
def modificar(request, id):
    productoModificado = Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductoForm(instance=productoModificado)
    }
    if request.method == 'POST':
        formularioo2 = ProductoForm(
            data=request.POST, instance=productoModificado)
        if formularioo2.is_valid:
            formularioo2.save()
            return redirect('Ventas')
    return render(request, 'modificar.html', datos)

@login_required
def eliminar(request, id):
    productoEliminado = Producto.objects.get(idProducto=id)
    productoEliminado.delete()
    return redirect('Ventas')

def mostrar(request):
    productis = Producto.objects.all()
    datos={
        'productis': productis
    }
    return render(request,'mostrar.html',datos)

def tienda(request):
    productis = Producto.objects.all()
    datos={
        'productis':productis
    }
    return render(request, 'tienda.html', datos)

def agregar_producto(request,id):
    print("Entrando a la función agregar_producto")
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.agregar(producto=producto) 
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.restar(producto=producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


def generarBoleta(request):
    precio_total = 0
    for key, value in request.session['carrito'].items():
        precio_total += int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total=precio_total)
    boleta = Boleta(total=precio_total, estado="Procesando Pedido")
    boleta.save()
    objetos = []
    for key, value in request.session['carrito'].items():
        objeto = Producto.objects.get(idProducto=value['idProducto'])
        cant = value['cantidad']
        subtotal = cant * int(value['precio'])
        detalle = detalle_boleta(id_boleta=boleta, idProducto=objeto, cantidad=cant, subtotal=subtotal)
        Producto.objects.filter(idProducto=objeto.idProducto).update(stock=F('stock') - cant)
        detalle.save()
        objetos.append(detalle)
    datos = {
        'objetos': objetos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html', datos)

