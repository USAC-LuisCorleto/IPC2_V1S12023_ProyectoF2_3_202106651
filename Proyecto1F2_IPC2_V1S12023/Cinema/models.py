from django.db import models

# Create your models here.
class Usuario(models.Model):
    rol = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    pelsFavs = []
    historialBoletos = []

class Película(models.Model):
    nombre_categoria = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    año_pelicula = models.IntegerField()
    fecha_funcion = models.DateField()
    hora_funcion = models.TimeField()
    imagen = models.URLField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Sala(models.Model):
    numero_sala = models.CharField(max_length=100)
    capacidad = models.IntegerField()

class Tarjeta(models.Model):
    tipo = models.CharField(max_length=50)
    numero = models.CharField(max_length=16)
    titular = models.CharField(max_length=100)
    fecha_expiracion = models.CharField(max_length=7) 
