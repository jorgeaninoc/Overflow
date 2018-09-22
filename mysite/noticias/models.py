from django.db import models

# Create your models here.

# Table Community
class Comunidad(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

# Table Product
class Producto(models.Model):
    name = models.CharField(max_length=255)
    price=models.IntegerField()
    community = models.ForeignKey(Comunidad,on_delete=models.CASCADE)


# Table Notice
class Notice(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    community = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

# Table Image
class Image(models.Model):
    path = models.CharField(max_length=255)

# Table User
class User(models.Model):
    password=models.CharField(max_length=255)
    name=models.CharField(max_length=150)
