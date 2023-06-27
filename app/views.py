from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProductoForm,ProveedorForm,PedidoForm
from .models import Producto,Proveedor,Pedido
from django.contrib import messages

# Create your views here.

def welcome(request):
    return render(request, "home.html")

@login_required
def proveedor(request):
    form = ProveedorForm()
    if request.method == 'POST':
        form=ProveedorForm(request.POST)
        if form.is_valid():
            print (form)
            proveedor=Proveedor()
            proveedor.rut=form.cleaned_data['rut']
            proveedor.nombre=form.cleaned_data['nombre']
            proveedor.razon_social=form.cleaned_data['razon_social']
            proveedor.save()
        else:
            print("Datos invalidos")
        return redirect('/proveedor')
    context = {'form': form}

    return render(request, 'proveedor.html', context=context)

@login_required
def producto(request):
    form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            print(form)
            producto = Producto()
            producto.sku = form.cleaned_data['sku']
            producto.nombre = form.cleaned_data['nombre']
            producto.cantidad = form.cleaned_data['cantidad']
            producto.categoria = form.cleaned_data['categoria']
            producto.fabricante = form.cleaned_data['fabricante']
            producto.precio = form.cleaned_data['precio']
            producto.save()
        else:
            print("Datos invalidos")
        return redirect('/producto')
    context = {'form': form}

    return render(request, 'producto.html', context=context)

@login_required
def pedido(request):
    form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            print(form)
            pedido = Pedido()
            pedido.nombre = form.cleaned_data['nombre']
            pedido.cantidad = form.cleaned_data['cantidad']
            pedido.save()
        else:
            print("Datos invalidos")
        return redirect('/pedido')
    context = {'form': form}

    return render(request, 'pedido.html', context=context)

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            permissions = form.cleaned_data['permissions']
            username = form.cleaned_data['username']
            user.groups.add(group)
            user.user_permissions.set(permissions)
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'register_user.html', context)

    
