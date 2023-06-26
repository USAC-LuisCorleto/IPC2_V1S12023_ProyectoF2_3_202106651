from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from .listaSimple import ListaEnlazada
from django.views.decorators.csrf import csrf_exempt

listaSimpleE = ListaEnlazada()
user="3082203580607"
password="202106651"
    
def MenInicialCerrarSesion(request):
    return render (request, "Cinema/menuSesion.html")

def MenInicial(request):
    return render (request, "Cinema/menuSesion.html")

@csrf_exempt
def MenIniciarSesion(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']

        if usuario == user and contraseña == password:
            return render(request, "Cinema/menuAdministrador.html")

    return render(request, "Cinema/sesionIniciar_Registrar.html")

@csrf_exempt
def MenRegUsuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']

        # Crea un nuevo objeto Usuario y guárdalo en la base de datos
        usuario = Usuario(rol='Cliente', nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, contraseña=contraseña)
        listaSimpleE.add(usuario)

        return redirect('menuCliente.html')

    return render (request, "Cinema/registroUser.html")

def MenCliente(request):
    return render (request, "Cinema/menuCliente.html")