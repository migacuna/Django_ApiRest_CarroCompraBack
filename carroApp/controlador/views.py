from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import serializers
from carroApp.serializers import AventuraSerializer, ReciboBoletaSerializer
from carroApp.servicios.services import VentaService
from carroApp.models import Aventura, ReciboBoleta


#Es la consulta base (Queryset) que utilizará el ViewSet para interactuar con la base de datos
# a través del ORM de Django. En lugar de traer todas las aventuras, 
# filtra estrictamente aquellas cuyo campo activo sea True
class AventuraViewSet(viewsets.ModelViewSet):
    queryset = Aventura.objects.filter(activo=True)
    serializer_class = AventuraSerializer #Conecta tu vista con el DTO (AventuraSerializer). 
    #Le indica al ViewSet qué clase debe utilizar para traducir de tabla de BDa Json
    
@api_view(['POST'])
@renderer_classes([JSONRenderer]) #decorador de Django Rest Framework (DRF) que fuerza a que la respuesta Json
def crea_compra_y_boleta(request):
    try:
        recibo = VentaService.procesar_compra(request.data)
        serializers = ReciboBoletaSerializer(recibo)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    


# Create your views here.

