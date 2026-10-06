from django.db import models
import uuid

# Create your models here.
class Aventura(models.Model):
        titulo = models.CharField(max_length=100)
        detalle = models.CharField(max_length=100)
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        imagen_url = models.URLField(max_length=500, blank=True, null=True)
        activo = models.BooleanField(default=True)
        
        def __str__(self):
                return f"{self.titulo} (${self.precio})"
            
class OrdenCacebera(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente_nombre = models.CharField(max_length=50)
    cliente_email = models.EmailField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default="APAGADO")
    fecha_creacion = models.DateField(auto_now_add=True)
    
class Ordendetalle(models.Model):
    orden = models.ForeignKey(OrdenCacebera,related_name="items", on_delete=models.CASCADE)
    aventura = models.ForeignKey(Aventura, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
class ReciboBoleta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orden = models.OneToOneField(OrdenCacebera, related_name='recibo', on_delete=models.CASCADE)
    codigo_canje = models.CharField(max_length=32, unique=True)
    instrucciones = models.TextField()
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    