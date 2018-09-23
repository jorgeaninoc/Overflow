from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django


# Create your models here.

# Table Image
class Image(models.Model):
    name = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

# Table Community
class Community(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=False)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.name

# Table Product
class Product(models.Model):
    name = models.CharField(max_length=255)
    price=models.IntegerField()
    community = models.ForeignKey(Community,on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)

    def __str__(self):

        return self.name

# Table Notice
class Notice(models.Model):
    title = models.CharField(max_length=255,null=False)
    text = models.TextField(null=False)
    endDate = models.DateField(default=django.utils.timezone.now() + django.utils.timezone.timedelta(30))
    startDate = models.DateField(default=django.utils.timezone.now())
    community = models.ForeignKey(Community,on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title


# Table Video
class Video(models.Model):
    url = models.CharField(max_length=255,unique=True,null=False)

    def __str__(self):
        return self.url

# Table IndexImages
class IndexImage(models.Model):
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

class GaleryImage(models.Model):
    name = models.CharField(max_length=255,unique=True,default=str(dt.now()))
    path = models.ImageField(upload_to="galery")

    def __str__(self):
        return self.name
