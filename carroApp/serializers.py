from rest_framework import serializers
from .models import Aventura, OrdenCacebera, Ordendetalle, ReciboBoleta

class AventuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aventura
        fields = '__all__'
        
class OrdenDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordendetalle
        fields = '__all__'
        
class OrdenCabeceraSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenCacebera
        fields = '__all__'
        #read_only_fields = ['id','estado', 'fecha_creacion']
        
class ReciboBoletaSerializer(serializers.ModelSerializer):
    orden_id = serializers.UUIDField(read_only=True)
    #cliente = serializers.CharField(source='orden.cliente_nombre', read_only=True)
    total_pagado = serializers.DecimalField(source='orden.monto_total', max_digits=10, decimal_places=2, read_only=True)
    items = OrdenDetalleSerializer(source='orden.items', many=True, read_only=True)
    
    class Meta:
        model = ReciboBoleta
        fields = '__all__'
        
#serializacion : transforma un objeto complejo de tu backend (objeto Django) a una cadena de texto JSON
#deserializacion : Toma la cadena Json a traves de un request http y la convierte en un estrucutra que python puede procesar        
# para desacoplar el sistema, permite que el front envie datos estructurados a Django sin importar el lenguaje y que los datos
#lleguen integros a la BD 

#Explicación exprés del Serializer (El DTO)
#El Serializer en DRF actúa como un puente inteligente y validador de datos.

#Valida: Revisa que el JSON que mande el frontend cumpla con las reglas (que los campos obligatorios existan, que los tipos de datos sean correctos).

#Mapea: Transforma ese JSON en diccionarios limpios de Python para que tu lógica de negocio o tus modelos puedan guardarlos directamente en la base de datos mediante el método .save() o .create().
        