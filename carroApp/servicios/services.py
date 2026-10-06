from django.db import transaction
from carroApp.models import OrdenCacebera, Ordendetalle, ReciboBoleta
import uuid

class VentaService:
    
    @staticmethod
    @transaction.atomic
    def procesar_compra(data):
        items_data = data.pop('items')
        
        monto_total = data.get('monto_total', 0)
        
        #Crear la cabecera de la Boleta
        orden = OrdenCacebera.objects.create(
            cliente_nombre = data.get('cliente_nombre'),
            cliente_email = data.get('cliente_email'),
            monto_total = monto_total
        )
        
        # Imprime esto en tu consola de Django antes de crear los detalles
        
        print("Objeto orden creado:", orden.id)
        
        #crear el detalle Boleta
        for item in items_data:
            print("ID de aventura recibido:", item['aventura'])
            Ordendetalle.objects.create(
                orden = orden,
                aventura_id = item['aventura'],
                cantidad = item['cantidad'],
                precio_unitario = item['precio_unitario']
            )
            
        #Generar Recibo / Boleta Automatica
        codigo = f"VTG-{uuid.uuid4().hex[:8].upper()}" #Genera un identificador universal único basado en números aleatorios (evita colisiones y duplicados).
        instrucciones = "1. Presenta este codigo en base 30 minutos antes. Lleva Ropa Comododa y agua"
        
        recibo = ReciboBoleta.objects.create(
            orden = orden,
            codigo_canje = codigo,
            instrucciones = instrucciones,
            total_pagado = orden.monto_total
        )
        
        return recibo