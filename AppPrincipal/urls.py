from django.urls import path
from . import views  

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'), 
]