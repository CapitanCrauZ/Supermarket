from django.urls import path

from .views import listarProducto, agregarProducto, modificarProducto, eliminarProducto
#, eliminarProducto
#, eliminarProducto

urlpatterns = [
    path('', listarProducto, name='listar_producto'),
    path('agregar/', agregarProducto, name='listar_producto'),
    path('modificar/<int:id_producto>', modificarProducto, name='listar_producto'),
    path('eliminar/<int:id_producto>', eliminarProducto, name='listar_producto'),
]