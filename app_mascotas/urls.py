from django.urls import path
from . import views

urlpatterns = [
    # URLs para Mascotas
    path('', views.inicio_mascotas, name='inicio_mascotas'),
    path('agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('ver/', views.ver_mascotas, name='ver_mascotas'),
    path('detalle/<int:id_animales>/', views.ver_detalle_mascota, name='detalle_mascota'),
    path('actualizar/<int:id_animales>/', views.actualizar_mascota, name='actualizar_mascota'),
    path('realizar-actualizacion/<int:id_animales>/', views.realizar_actualizacion_mascota, name='realizar_actualizacion_mascota'),
    path('borrar/<int:id_animales>/', views.borrar_mascota, name='borrar_mascota'),
    
    # NUEVAS URLs para Clientes
    path('clientes/', views.inicio_clientes, name='inicio_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_clientes, name='ver_clientes'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar-actualizacion/<int:id_cliente>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
]