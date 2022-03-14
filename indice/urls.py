from django.urls import path
from .views import inicio,otra_vista,numeros_random,numero_del_usuario, mi_plantilla
    
urlpatterns = [
    path('inicio/', inicio),
    path('', otra_vista),
    path('numero-random/', numeros_random),
    path('dame-numero/<numero>', numero_del_usuario),
    #path('dame-numero/<int:numero>', numero_del_usuario),
    path('mi-plantilla/', mi_plantilla)
    ]