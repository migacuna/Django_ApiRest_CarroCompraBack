from django.urls import path, include
from carroApp.controlador import views
from rest_framework.routers import DefaultRouter
from carroApp.controlador.views import AventuraViewSet

# el router genera automaticamente las rutas standars para el ViewSet (listar, crear, ver detalle, etc)
# Le dice a Django: "Crea automáticamente todas las URLs estándar de una API REST 
# (Listar, Crear, Ver detalle, Actualizar, Borrar) para el AventuraViewSet bajo la ruta /aventuras/". 
# (Por ejemplo: GET /aventuras/, POST /aventuras/, etc.).
router = DefaultRouter()
router.register(r'aventuras', AventuraViewSet, basename="aventura")

urlpatterns = [
    path('', include(router.urls)),
    path('comprar/', views.crea_compra_y_boleta, name="procesar-compra")
]
