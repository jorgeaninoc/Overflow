from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django

# Create your models here.

# Table Image
class Imagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

# Table Community
class Comunidad(models.Model):
    nombre = models.CharField(max_length=255,unique=True,null=False)
    descripcion = models.TextField(null=False)
    imagenes = models.ManyToManyField(Imagen)

    def __str__(self):
        return self.nombre

# Table Product
class Producto(models.Model):
    nombre = models.CharField(max_length=255,null=False)
    precio=models.IntegerField(null=False)
    communidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen,null=False)

    def __str__(self):
        return self.nombre

# Table Notice
class Noticia(models.Model):
    titulo = models.CharField(max_length=255,null=False)
    texto = models.TextField(null=False)
    fechaInicio = models.DateField(default=django.utils.timezone.now())
    fechaFin = models.DateField(default=django.utils.timezone.now() + django.utils.timezone.timedelta(30))
    comunidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen)

    def __str__(self):
        return self.titulo


# Table Video
class Video(models.Model):
    url = models.CharField(max_length=255,unique=True,null=False)

    def __str__(self):
        return self.url

# Table IndexImages
class InicioImagen(models.Model):
    nombre = models.CharField(max_length=255,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre


class GaleriaImagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

class ColaboraImagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

class Valor(models.Model):
    valor = models.TextField(null=False)
    valoresImagen = models.ImageField(upload_to="images")

    def __str__(self):
        return self.valor

class Politica(models.Model):
    politica = models.CharField(max_length=255,null=False)
    def __str__(self):
        return self.politica

class Somos(models.Model):
    titulo = models.CharField(max_length=255,null=False)

class Vision(models.Model):
    vision=models.TextField(null=False)
    visionImagen = models.ImageField(upload_to="images")

    def __str__(self):
        return self.titulo

class Mision(models.Model):
    mision = models.TextField(null=False)
    imagen =  models.ImageField(upload_to="images")


class Colaborador(models.Model):
    nombre= models.CharField(max_length=255,null=False)
    telefono=models.CharField(max_length=20)
    correo=models.EmailField()
    empresa=models.CharField(max_length=255)

class Contacto(models.Model):
    telefono = models.CharField(max_length=255,null=False)
    horario = models.CharField(max_length=255,null=False)
    mail = models.EmailField(null=False)

class Mensaje(models.Model):
    nombre =  models.CharField(max_length=255,null=False)
    correo = models.EmailField(null=False)
    mensaje = models.CharField(max_length=255,null=False)
