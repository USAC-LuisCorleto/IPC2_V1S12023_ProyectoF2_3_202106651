from django.contrib import admin
from django.urls import path
from Cinema.views import MenInicial
from Cinema.views import MenIniciarSesion
from Cinema.views import MenRegUsuario
from Cinema.views import MenCliente
from Cinema.views import MenInicialCerrarSesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cinema/', MenInicial, name='Cinema'),
    path('Cinema/sesionIniciar_Registrar.html', MenIniciarSesion, name='Registrar_Sesión'),
    path('Cinema/registroUser.html', MenRegUsuario, name='Registrar_usuario'),
    path('Cinema/menuCliente.html', MenCliente, name='Menu_Cliente'),
    path('Cinema/menuSesion.html', MenInicialCerrarSesion, name='Regresar_MenInicial'),
]
