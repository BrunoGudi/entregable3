from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insertar-datos/', views.insertar_datos, name='insertar_datos'),
    path('buscar-datos/', views.buscar_datos, name='buscar_datos'),
]