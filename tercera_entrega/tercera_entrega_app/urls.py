from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_orden/', views.agregar_orden, name='agregar_orden'),
]
