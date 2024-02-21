
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('index/', views.index, name='index'),
    path('registroCatalogos/', views.registrarCatalogos, name='registrar_catalogos'),
    path('eliminarMarcas/<codigo>/',
         views.eliminarMarcas, name='eliminar_marcas'),
    path('eliminarPresentaciones/<codigo>/',
         views.eliminarPresentaciones, name='eliminar_presentaciones'),     
    path('eliminarProducto/<codigo>/',
         views.eliminarProducto, name='eliminar_producto'),     
    path('registroProductos/', views.registrar_productos, name='registrar_productos'), 
    path('editar_producto_modal/<int:producto_id>/', views.editar_producto_modal, name='editar_producto_modal'),   
    path('editar_presentaciones_modal/<int:presentaciones_id>/', views.editar_presentaciones_modal, name='editar_presentaciones_modal'),
    path('editar_marcas_modal/<int:marcas_id>/', views.editar_marcas_modal, name='editar_marcas_modal'),      
]