from django.shortcuts import render
    
def MenInicial(request):
    return render (request, "Cinema/menuSesion.html")

def MenIniciarSesion(request):
    return render (request, "Cinema/sesionIniciar_Registrar.html")

def MenRegUsuario(request):
    return render (request, "Cinema/registroUser.html")