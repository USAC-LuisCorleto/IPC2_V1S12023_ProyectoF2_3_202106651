from django.db import models
from PIL import Image

# Create your models here.
class Usuario(models.Model):
    rol = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)

class Película(models.Model):
    nombre_categoria = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    año_pelicula = models.IntegerField()
    fecha_funcion = models.DateField()
    hora_funcion = models.TimeField()
    imagen = models.ImageField(upload_to='assets')
    precio = models.DecimalField(max_digits=6, decimal_places=2)
