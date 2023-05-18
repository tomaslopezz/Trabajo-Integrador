from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm

# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'lista_productos.jinja', context)

def crear_producto(request):
    form = ProductoForm()

    if request.method == "POST":

        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('crear_producto')



        else:
            return HttpResponseRedirect('crear_producto')
        
    context = {'form':form}
    
    return render(request, 'crear_producto.jinja', context)

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {'proveedores':proveedores}
    return render(request, 'lista_proveedores.jinja', context)


def crear_proveedor(request):
    form = ProveedorForm()

    if request.method == "POST":

        form = ProveedorForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/crear_proveedor/')




        else:
            return HttpResponseRedirect('/crear_proveedor/')
        
    context = {'form':form}
    
    return render(request, 'crear_proveedor.jinja', context)

