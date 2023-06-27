from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from .models import Película
from .listaSimple import ListaEnlazada
from django.views.decorators.csrf import csrf_exempt
from .listaDobleC import ListaDoblementeEnlazadaCircular

listaSimpleE = ListaEnlazada()
listaDobleE = ListaDoblementeEnlazadaCircular()
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
        usuario_encontrado = listaSimpleE.buscar_usuario(usuario,contraseña)
        if usuario_encontrado is not None:
            return render (request, "Cinema/menuCliente.html")
    return render(request, "Cinema/sesionIniciar_Registrar.html")

@csrf_exempt
def MenRegUsuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']

        usuario = Usuario(rol='Cliente', nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, contraseña=contraseña)
        listaSimpleE.add(usuario)
        listaSimpleE.generar_archivo_XML()
        return redirect('menuCliente.html')

    return render (request, "Cinema/registroUser.html")

def MenCliente(request):
    return render (request, "Cinema/menuCliente.html")

@csrf_exempt
def MenCrearUsuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']

        usuario = Usuario(rol='Cliente', nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, contraseña=contraseña)
        listaSimpleE.add(usuario)
        listaSimpleE.generar_archivo_XML()
        return redirect('menuAdministrador.html')
    
    return render (request, "Cinema/crearUsuario.html")

def MenAdministrador(request):
    return render (request, "Cinema/menuAdministrador.html")

@csrf_exempt
def MenEditarUsuario(request):
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            correo = request.POST['correo']
            listaSimpleE.eliminar_usuario(correo)
            return redirect('editarUsuario.html')

        correo = request.POST['correo']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        contraseña = request.POST['contraseña']

        listaSimpleE.actualizar_usuario(correo, nombre, apellido, telefono, contraseña)

        return redirect('editarUsuario.html')

    lista_usuarios = listaSimpleE.obtener_lista_usuarios()

    context = {
        'lista_usuarios': lista_usuarios,
    }

    return render(request, "Cinema/editarUsuario.html", context)

@csrf_exempt
def MenCargarUsuarios(request):
    if request.method == 'POST':
        archivo = request.POST['archivo']
        listaSimpleE.cargar_desde_xml(archivo)
        listaSimpleE.generar_archivo_XML()  
        return redirect('menuAdministrador.html')
    

    return render(request, "Cinema/cargarUsuario.html")

def MenCrearPelícula(request):
    if request.method == 'POST':
        nombre_categoria = request.POST['nombre_categoria']
        titulo = request.POST['titulo']
        director = request.POST['director']
        año_pelicula = int(request.POST['año_pelicula'])
        fecha_funcion = request.POST['fecha_funcion']
        hora_funcion = request.POST['hora_funcion']
        imagen = request.FILES['imagen']
        precio = request.POST['precio']

        pel = Película(nombre_categoria=nombre_categoria, titulo=titulo, director=director, año_pelicula=año_pelicula, fecha_funcion=fecha_funcion, hora_funcion=hora_funcion, imagen=imagen, precio=precio)
        listaDobleE.add(pel)
        listaDobleE.guardar_en_xml()
        return redirect('menuAdministrador.html')
    
    return render(request, "Cinema/crearPelícula.html")

def MenEditPelícula(request):
    lista_peliculas = listaDobleE.obtener_lista_peliculas()
    if request.method == 'POST':
        titulo = request.POST['titulo']
        nuevo_titulo = request.POST['nuevo_titulo']
        director = request.POST['director']
        año_pelicula = int(request.POST['año_pelicula'])
        fecha_funcion = request.POST['fecha_funcion']
        hora_funcion = request.POST['hora_funcion']
        imagen = request.FILES['imagen']
        precio = request.POST['precio']

        # Aquí debes llamar al método actualizar_pelicula de tu lista doblemente enlazada
        # pasando los parámetros correspondientes
        listaDobleE.actualizar_pelicula(titulo, nuevo_titulo, director, año_pelicula, fecha_funcion, hora_funcion, imagen, precio)

        return redirect('menuAdministrador.html')

    return render(request, "Cinema/editarPelícula.html", {'lista_peliculas': lista_peliculas})


