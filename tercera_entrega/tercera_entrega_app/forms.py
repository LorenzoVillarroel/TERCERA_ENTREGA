from django import forms
from .models import Cliente, Producto, Orden

class BuscarClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, label='Nombre del Cliente')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['cliente', 'producto', 'cantidad']
