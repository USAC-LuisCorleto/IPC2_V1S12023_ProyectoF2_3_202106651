from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from .models import Película
from .models import Sala
from .models import Tarjeta
from django.views.decorators.csrf import csrf_exempt
from .listaSimple import ListaEnlazada
from .listaDobleC import ListaDoblementeEnlazadaCircular
from .listaDoble import ListaDoblementeEnlazada
from .listaDobleT import ListaDoblementeEnlazadaT
import requests

usuario_encontrado = None
listaSimpleE = ListaEnlazada()
listaDobleE = ListaDoblementeEnlazadaCircular()
ListaDoble = ListaDoblementeEnlazada()
ListaDobleT = ListaDoblementeEnlazadaT()
incremento = 0
datos_cargados = False
user="3082203580607"
password="202106651"
    
def MenInicialCerrarSesion(request):
    return render (request, "Cinema/menuSesion.html")

def MenInicial(request):
    return render (request, "Cinema/menuSesion.html")

@csrf_exempt
def MenIniciarSesion(request):
    global usuario_encontrado 

    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']

        if usuario == user and contraseña == password:
            return render(request, "Cinema/menuAdministrador.html")
        
        usuario_encontrado = listaSimpleE.buscar_usuario(usuario, contraseña)
        if usuario_encontrado is not None:
            return render(request, "Cinema/menuCliente.html")
        else:
            mensaje = "El usuario ingresado no existe. Regístrese o verifique sus credenciales."
            return render(request, "Cinema/sesionIniciar_Registrar.html", {'mensaje': mensaje})
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
        return redirect('menuSesion.html')

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

        response = requests.get('http://localhost:5007/getUsuarios')
        usuarios_API = response.json()

        for usuario in usuarios_API['usuarios']:
            rol = usuario['rol']
            nombre = usuario['nombre']
            apellido = usuario['apellido']
            telefono = usuario['telefono']
            correo = usuario['correo']
            contraseña = usuario['contrasena']

            nuevo_usuario = Usuario(rol=rol, nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, contraseña=contraseña)
            listaSimpleE.add(nuevo_usuario)

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

@csrf_exempt
def MenEditPelícula(request):
    lista_peliculas = listaDobleE.obtener_lista_peliculas()

    if request.method == 'POST':
        if 'eliminar' in request.POST:
            titulo = request.POST.get('titulo', '')
            listaDobleE.eliminar_pelicula(titulo)
            listaDobleE.eliminar_pelicula_del_xml(titulo)
            return redirect('editarPelícula.html')

        nuevo_titulo = request.POST['titulo']
        director = request.POST['director']
        año_pelicula = int(request.POST['año_pelicula'])
        fecha_funcion = request.POST['fecha_funcion']
        hora_funcion = request.POST['hora_funcion']
        precio = request.POST['precio']

        listaDobleE.actualizar_pelicula(nuevo_titulo, director, año_pelicula, fecha_funcion, hora_funcion, precio)
        listaDobleE.guardar_en_xml()

        return redirect('editarPelícula.html')

    return render(request, "Cinema/editarPelícula.html", {'lista_peliculas': lista_peliculas})

@csrf_exempt
def MenCargarPelícula(request):
    if request.method == 'POST':
        archivo = request.POST['archivo']
        listaDobleE.cargar_desde_xml(archivo)
        listaDobleE.guardar_en_xml() 
        response = requests.get('http://localhost:5009/getPeliculas')
        peliculas_API = response.json()

        for categoria in peliculas_API['categoria']:
            nombre_categoria = categoria['nombre']
            peliculas = categoria['peliculas']['pelicula']

            for pelicula in peliculas:
                titulo = pelicula['titulo']
                director = pelicula['director']
                año_pelicula = pelicula['anio']
                fecha_funcion = pelicula['fecha']
                hora_funcion = pelicula['hora']
                imagen = pelicula['imagen']
                precio = pelicula['precio']

                nueva_pelicula = Película(nombre_categoria=nombre_categoria, titulo=titulo, director=director, año_pelicula=año_pelicula, fecha_funcion=fecha_funcion, hora_funcion=hora_funcion, imagen=imagen, precio=precio)
                listaDobleE.add(nueva_pelicula)
                
        return redirect('menuAdministrador.html')
    return render(request, "Cinema/cargarPelícula.html")

@csrf_exempt
def MenCrearSala(request):
    global incremento

    if request.method == 'POST':
        incremento += 1 
        no_sala = f"#USACIPC2_202106651_{incremento}"
        asientos = request.POST['Asientos']

        sala = Sala(numero_sala=no_sala, capacidad=asientos) 
        ListaDoble.add(sala)
        ListaDoble.guardar_en_xml()
        return redirect('menuAdministrador.html')

    return render(request, "Cinema/crearSala.html")

@csrf_exempt
def MenEditarSala(request):
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            numero_sala = request.POST['numero']
            ListaDoble.eliminar_sala(numero_sala)
            return redirect('editarSala.html')

        nuevo_no_sala = request.POST['numero']
        nueva_capacidad = request.POST['capacidad']

        ListaDoble.actualizar_sala(nuevo_no_sala, nueva_capacidad)
        return redirect('editarSala.html')

    lista_salas = ListaDoble.obtener_lista_salas()

    context = {
        'lista_salas': lista_salas,
    }
    return render(request, "Cinema/editarSala.html", context)

def MenCargarSala(request):
    global datos_cargados
    
    if request.method == 'POST':
        archivo = request.POST['archivo']
        
        if datos_cargados:
            return redirect('menuAdministrador.html')
        
        ListaDoble.cargar_desde_xml(archivo)
        ListaDoble.guardar_en_xml()

        response = requests.get('http://localhost:5008/getSalas')
        salas_API = response.json()

        for cine in salas_API['cines']:
            salas = cine['salas']

            for sala in salas:
                numero_sala = sala['numero']
                capacidad = sala['asientos']

                nueva_sala = Sala(numero_sala=numero_sala, capacidad=capacidad)
                ListaDoble.add(nueva_sala)

        datos_cargados = True

        return redirect('menuAdministrador.html')

    return render(request, "Cinema/cargarSala.html")

@csrf_exempt
def MenCrearTarjeta(request):
    if request.method == 'POST':
        tipot = request.POST['tipo']
        titulart = request.POST['numero']
        numerot = request.POST['titular']
        fechat = request.POST['expiración']

        tarjeta = Tarjeta(tipo=tipot, numero=numerot, titular=titulart, fecha_expiracion=fechat)
        ListaDobleT.agregar(tarjeta)
        ListaDobleT.generar_archivo_xml()
        return redirect('menuAdministrador.html')
    
    return render(request, "Cinema/crearTarjeta.html")

@csrf_exempt
def MenEditarTarjeta(request):
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            numero_tarjeta = request.POST['numero']
            ListaDobleT.eliminar_tarjeta(numero_tarjeta)
            return redirect('editarTarjeta.html')

        numero_tarjeta = request.POST['numero']
        nuevo_no_tarjeta = request.POST['numero']
        nuevo_titular = request.POST['titular']
        nueva_fecha_expiracion = request.POST['fecha_expiracion']

        ListaDobleT.actualizar_tarjeta(numero_tarjeta, nuevo_no_tarjeta, nuevo_titular, nueva_fecha_expiracion)
        return redirect('editarTarjeta.html')

    lista_tarjetas = ListaDobleT.obtener_lista_tarjetas()

    context = {
        'lista_tarjetas': lista_tarjetas,
    }
    return render(request, "Cinema/editarTarjeta.html", context)

def MenCargarTarjeta(request):
    if request.method == 'POST':

        archivo = request.POST['archivo']
        ListaDobleT.cargar_desde_xml(archivo)
        ListaDobleT.generar_archivo_xml()

        response = requests.get('http://localhost:5010/getTarjetas')
        tarjetas_API = response.json()

        for tarjeta in tarjetas_API['tarjetas']:
            tipon = tarjeta['tipo']
            numeron = tarjeta['numero']
            titularn = tarjeta['titular']
            fechan = tarjeta['fecha_expiracion']

            nueva_tarjeta = Tarjeta(tipo=tipon, numero=numeron, titular=titularn, fecha_expiracion=fechan)
            ListaDobleT.agregar(nueva_tarjeta)

        return redirect('menuAdministrador.html')
    
    return render(request, "Cinema/cargarTarjeta.html")

@csrf_exempt
def MenPeliculasFavoritas(request):
    global usuario_encontrado
    lista_peliculas = listaDobleE.obtener_lista_peliculas()
    mensaje = None  # Inicializamos la variable mensaje

    if request.method == 'POST':
        peliFav = request.POST.get('peliculaFav')

        if usuario_encontrado is not None:
            if peliFav in [pelicula.titulo for pelicula in lista_peliculas]:
                usuario_encontrado.pelsFavs.append(peliFav)
                mensaje = "Película agregada correctamente"
            else:
                mensaje = "La película no existe en la lista"

    return render(request, "Cinema/menuPeliculasFavs.html", {'lista_peliculas': lista_peliculas, 'mensaje': mensaje})

def MenVerPelisFavs(request):
    global usuario_encontrado
    peliculas_favoritas = usuario_encontrado.pelsFavs

    return render(request, "Cinema/menuVerPeliculas.html", {'peliculas_favoritas': peliculas_favoritas})

