# Django_ApiRest_CarroCompraBack
ApiRest Carro de Compra, desarrollado en Python con Django y Base de datos. Para arquitectura Microservicio, donde revice peticiones HTTP desde un una pagina Web, Ecommerce, visualiza catalogo de productos, procesa compra y emite boleta.

Este se conecta directamente con el Front (Pagina Web, tipo ecommerce, muestra catalogo de productos, almacenados en un base de datos, la cual se accede a traves de la ApiRest).

## 🏛️ Arquitectura del Sistema
![Diagrama de Arquitectura](./docs/Arquitectura_CarroCompra.png)


Implementación: Descargue y levante la Apirest localhost:8000, recordar que antes de levantarlo, debe migrar la base de datos:
python manage.py makemigrations - python manage.py migrate
Luego de migrar debe ingresar a la base de datos, para insertar o agregar los productos y para eso debe crear el superusuario para el /admin de Django

ademas debe instalar libreria de rest_framework y cors-headers:

pip install djangorestframework
pip install django-cors-headers
