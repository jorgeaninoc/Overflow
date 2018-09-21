from django.db import models

# Create your models here.
"""
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
"""

# Table Product
class Producto(models.Model):
    name = models.CharField(max_length=255)
    price=models.IntegerField()
    community = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

# Table Community
class Comunidad(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

# Table Notice
class Notice(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    community = models.ForeignKey(Comunidad,on_delete=models.CASCADE)
