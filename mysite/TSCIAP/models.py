from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
from django.utils import timezone

# Create your models here.

# Table Community
class Community(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name

# Table Product
class Product(models.Model):
    name = models.CharField(max_length=255)
    price=models.IntegerField()
    community = models.ForeignKey(Community,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Table Notice
class Notice(models.Model):
    title = models.CharField(max_length=255,null=False)
    text = models.TextField(null=False)
    endDate = models.DateField(default=timezone.now()+ timezone.timedelta(30))
    startDate = models.DateField(default=timezone.now())
    community = models.ForeignKey(Community,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Table Image
class Image(models.Model):
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.path

# Table Video
class Video(models.Model):
    url = models.CharField(max_length=255,unique=True,null=False)

    def __str__(self):
        return self.url

# Table IndexImages
class IndexImage(models.Model):
    path = models.ImageField(upload_to="images")

    def __str__(self):
        return self.path
