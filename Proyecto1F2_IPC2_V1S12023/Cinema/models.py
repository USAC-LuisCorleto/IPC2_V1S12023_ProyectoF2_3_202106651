from django.db import models

# Create your models here.
class Usuario(models.Model):
    rol = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)