from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('EP', 'En Preparacion'),
        ('ED', 'En Despacho'),
        ('E', 'Entregado'),
    ]
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES, default='P')
    cancelado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre



