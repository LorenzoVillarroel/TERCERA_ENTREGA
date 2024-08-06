# tercera_entrega_app/views.py
from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, OrdenForm, BuscarClienteForm
from .models import Cliente

def index(request):
    return render(request, 'tercera_entrega_app/index.html')

def buscar_cliente(request):
    form = BuscarClienteForm(request.GET or None)
    clientes = None
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            clientes = Cliente.objects.filter(nombre__icontains=nombre)
    return render(request, 'tercera_entrega_app/buscar_cliente.html', {'form': form, 'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'tercera_entrega_app/agregar_cliente.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'tercera_entrega_app/agregar_producto.html', {'form': form})

def agregar_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrdenForm()
    return render(request, 'tercera_entrega_app/agregar_orden.html', {'form': form})
