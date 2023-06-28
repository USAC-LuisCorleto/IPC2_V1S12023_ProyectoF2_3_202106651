from django.contrib import admin
from django.urls import path
from Cinema.views import MenInicial
from Cinema.views import MenIniciarSesion
from Cinema.views import MenRegUsuario
from Cinema.views import MenCliente
from Cinema.views import MenInicialCerrarSesion
from Cinema.views import MenCrearUsuario
from Cinema.views import MenAdministrador
from Cinema.views import MenEditarUsuario
from Cinema.views import MenCargarUsuarios
from Cinema.views import MenCrearPelícula
from Cinema.views import MenEditPelícula
from Cinema.views import MenCargarPelícula
from Cinema.views import MenCrearSala

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cinema/', MenInicial, name='Cinema'),
    path('Cinema/sesionIniciar_Registrar.html', MenIniciarSesion, name='Registrar_Sesión'),
    path('Cinema/registroUser.html', MenRegUsuario, name='Registrar_usuario'),
    path('Cinema/menuCliente.html', MenCliente, name='Menu_Cliente'),
    path('Cinema/menuSesion.html', MenInicialCerrarSesion, name='Regresar_MenInicial'),
    path('Cinema/crearUsuario.html', MenCrearUsuario, name='CrearUsuario_Admin'),
    path('Cinema/menuAdministrador.html', MenAdministrador, name='Menu_administrador'),
    path('Cinema/editarUsuario.html', MenEditarUsuario, name='Menu_EditarUsuario'),
    path('Cinema/cargarUsuario.html', MenCargarUsuarios, name='Men_CargarUsuario'),
    path('Cinema/crearPelícula.html', MenCrearPelícula, name='Men_CrearPelícula'),
    path('Cinema/editarPelícula.html', MenEditPelícula, name='Men_EditarPelícula'),
    path('Cinema/cargarPelícula.html', MenCargarPelícula, name='Men_CargarPelícula'),
    path('Cinema/crearSala.html', MenCrearSala, name='Men_CrearSala'),
]
