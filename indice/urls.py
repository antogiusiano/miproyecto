from django.urls import path
from .views import inicio,otra_vista,numeros_random,numero_del_usuario, mi_plantilla, login, registrar, editar
from django.contrib.auth.views import LogoutView
 
urlpatterns = [
    path('', inicio, name='inicio'),
    path('otra-vista/', otra_vista, name = 'otra_vista'),
    path('numero-random/', numeros_random, name = 'numero_random'),
    path('dame-numero/<numero>', numero_del_usuario, name = 'dame_numero'),
    #path('dame-numero/<int:numero>', numero_del_usuario),
    path('mi-plantilla/', mi_plantilla, name = 'mi_plantilla'),
    path('login/', login, name = 'login'),
    path('registrar/', registrar, name = 'registrar'),
    path('editar/', editar, name = 'editar'),
    path('logout', LogoutView.as_view(template_name='indice/logout.html'), name = 'logout')
]