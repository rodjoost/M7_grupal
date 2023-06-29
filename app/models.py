from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proveedor(models.Model):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)

    
class Producto(models.Model):
    sku = models.IntegerField()
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    precio = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor,null=True, on_delete=models.SET_NULL)



class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()  






