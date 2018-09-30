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

    class Meta:
        verbose_name: "Imagen"
        verbose_name_plural = "Imagenes"

# Table Community
class Comunidad(models.Model):
    nombre = models.CharField(max_length=255,unique=True,null=False)
    descripcion = models.TextField(null=False)
    imagenes = models.ManyToManyField(Imagen)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Comunidad"
        verbose_name_plural = "Comunidades"


# Table Product
class Producto(models.Model):
    nombre = models.CharField(max_length=255,null=False)
    precio=models.IntegerField(null=False)
    communidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Producto"
        verbose_name_plural = "Productos"

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

    class Meta:
        verbose_name: "Noticia"
        verbose_name_plural = "Noticias"

# Table Video
class Video(models.Model):
    url = models.CharField(max_length=255,unique=True,null=False)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name: "Video"
        verbose_name_plural = "Videos"

# Table IndexImages
class InicioImagen(models.Model):
    nombre = models.CharField(max_length=255,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Imagen de Inicio"
        verbose_name_plural = "Imagenes de Inicio"


class GaleriaImagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Imagen de Galeria"
        verbose_name_plural = "Imagenes de Galeria"

class ColaboraImagen(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Imagen de Colabora"
        verbose_name_plural = "Imagenes de Colabora"

class Valor(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    valor = models.TextField(null=False)
    valoresImagen = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Valor de Somos"
        verbose_name_plural = "Valores de Somos"

class Politica(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    politica = models.TextField(null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Politica de Somos"
        verbose_name_plural = "Politicas de Somos"

class Somos(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    titulo = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Titulo de Somos"
        verbose_name_plural = "Titulos de Somos"

class Vision(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    vision=models.TextField(null=False)
    visionImagen = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Vision de Somos"
        verbose_name_plural = "Visiones de Somos"



class Mision(models.Model):
    nombre = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    mision = models.TextField(null=False)
    imagen =  models.ImageField(upload_to="images")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Mision de Somos"
        verbose_name_plural = "Misiones de Somos"


class Colaborador(models.Model):
    nombre= models.CharField(max_length=255,null=False)
    telefono=models.CharField(max_length=20)
    correo=models.EmailField()
    empresa=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Colaborador"
        verbose_name_plural = "Colaboradores"

class Contacto(models.Model):
    telefono = models.CharField(max_length=255,null=False)
    horario = models.CharField(max_length=255,null=False)
    mail = models.EmailField(null=False)

    class Meta:
        verbose_name: "Informacion de Contacto"
        verbose_name_plural = "Informacion de Contacto"

class Mensaje(models.Model):
    nombre =  models.CharField(max_length=255,null=False)
    correo = models.EmailField(null=False)
    mensaje = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: "Mensaje"
        verbose_name_plural = "Mensajes"


class Anuncio(models.Model):
    titulo = models.CharField(max_length=255,null=False)
    texto = models.TextField(null=False)
    imagenes = models.ManyToManyField(Imagen)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name: "Anuncio"
        verbose_name_plural = "Anuncios"
