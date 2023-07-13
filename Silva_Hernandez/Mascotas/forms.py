from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria,Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']





class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'precio', 'stock', 'imagen', 'descripcion','categoria']
        labels = {
            'idProducto': 'idProducto',
            'precio': 'precio',
            'stock': 'stock',
            'imagen': 'Imagen',
            'descripcion':'descripcion',
            'categoria': 'Categoria'
        }
        widgets = {
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese la Id del Producto',
                    'id': 'idProducto',
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio',
                    'id': 'marca',
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese stock..',
                    'id': 'stock',
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'class': 'form-control',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese descripcion..',
                    'id':'descripcion',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id':'categoria',
                }
            )    
        }
    