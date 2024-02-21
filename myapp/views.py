from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Marca, Presentacion,Producto
from .forms import MarcaForm, PresentacionForm, ProductoForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return render(request, "index.html")
def inicio(request):

    return render(request, "inicio.html")

def registrarCatalogos(request):
    form_marcas = MarcaForm()
    form_presentaciones = PresentacionForm()
    marcas = Marca.objects.all()
    presentaciones = Presentacion.objects.all()
    if request.method == 'POST':
        if 'guardarFormMarcas' in request.POST:
            form_marcas = MarcaForm(request.POST)
            if form_marcas.is_valid():
                form_marcas.save()
                messages.success(request, 'Registro de marca exitoso!')
                return redirect(request.get_full_path()) 

        elif 'guardarFormPresentaciones' in request.POST:
            form_presentaciones = PresentacionForm(request.POST)
            if form_presentaciones.is_valid():
                form_presentaciones.save()
                messages.success(request, 'Registro de presentación exitoso!')
                return redirect(request.get_full_path()) 
            
    active_tab = request.GET.get('tab', 'marcas')

    context = {
        'form_marcas': form_marcas,
        'form_presentaciones': form_presentaciones,
        'marcas': marcas,
        'presentaciones': presentaciones,
        'active_tab': active_tab,
    }

    return render(request, 'registroCatalogos.html', context)

def eliminarMarcas(request, codigo):
    marcas = Marca.objects.get(id=codigo)
    marcas.delete()
    messages.success(request, 'Eliminado!')
    return redirect(reverse('registrar_catalogos') + '?tab=marcas')

def eliminarPresentaciones(request, codigo):
    presentaciones = Presentacion.objects.get(id=codigo)
    presentaciones.delete()
    messages.success(request, 'Eliminado!')
    return redirect(reverse('registrar_catalogos') + '?tab=presentaciones')

def eliminarProducto(request, codigo):
    productos = Producto.objects.get(id=codigo)
    productos.delete()
    messages.success(request, 'Eliminado!')
    return redirect('registrar_productos')

def registrar_productos(request):
    form_productos = ProductoForm()
    productos = Producto.objects.all()

    if request.method == 'POST':
        form_productos = ProductoForm(request.POST)
        if form_productos.is_valid():
            form_productos.save()
            messages.success(request, 'Producto registrado exitosamente!')
            return redirect(request.get_full_path())  

    context = {
        'form_productos': form_productos,
        'productos': productos,
    }

    return render(request, 'registroProductos.html', context)

def editar_producto_modal(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('registrar_productos')
    else:
        form = ProductoForm(instance=producto) 
    
    context = {
        'form': form,
        'producto': producto,
    }
    
    return render(request, 'editarProductoModal.html', context)

def editar_presentaciones_modal(request, presentaciones_id):
    presentaciones = get_object_or_404(Presentacion, id=presentaciones_id)
    
    if request.method == 'POST':
        form = PresentacionForm(request.POST, instance=presentaciones)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect(reverse('registrar_catalogos') + '?tab=presentaciones')
    else:
        form = PresentacionForm(instance=presentaciones) 
    
    context = {
        'form': form,
        'presentaciones': presentaciones,
    }
    
    return render(request, 'edicionPresentacionesModal.html', context)

def editar_marcas_modal(request, marcas_id):
    marcas = get_object_or_404(Marca, id=marcas_id)
    
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marcas)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect(reverse('registrar_catalogos') + '?tab=marcas')
    else:
        form = MarcaForm(instance=marcas) 
    
    context = {
        'form': form,
        'marcas': marcas,
    }
    
    return render(request, 'edicionMarcasModal.html', context)