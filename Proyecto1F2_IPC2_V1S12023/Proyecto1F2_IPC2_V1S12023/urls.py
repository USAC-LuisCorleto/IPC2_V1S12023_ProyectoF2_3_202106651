from django.contrib import admin
from django.urls import path
from Cinema.views import MenInicial
from Cinema.views import MenIniciarSesion
from Cinema.views import MenRegUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cinema/', MenInicial, name='Cinema'),
    path('Cinema/sesionIniciar_Registrar.html', MenIniciarSesion, name='Registrar_Sesión'),
    path('Cinema/registroUser.html', MenRegUsuario, name='Registrar_usuario'),
]
