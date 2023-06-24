from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from .models import Producto, Proveedor, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

        form_fields = ['sku', 'nombre', 'cantidad', 'categoria', 'fabricante', 'precio']
        for field in form_fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
     

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)

        form_fields = ['rut', 'nombre', 'razon_social']
        for field in form_fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class PedidoForm(forms.ModelForm):
    class Meta:
        model= Pedido
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)

        form_fields = ['nombre', 'cantidad']
        for field in form_fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
