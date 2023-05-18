from django.urls import path
from . import views

urlpatterns = [
    path('productos/lista_productos', views.listar_productos, name='lista_productos'),
    path('productos/crear_producto', views.crear_producto, name='crear-producto'),
    path('proveedores/lista_proveedores', views.listar_proveedores, name="lista_proveedores" ),
    path('proveedores/crear_proveedor', views.crear_proveedor, name='crear-proveedor')

]