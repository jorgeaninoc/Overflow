from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.db import models
from Catalogo.models import *

from django.db import models
from datetime import timedelta as td
from datetime import datetime as dt
import django

class Perfil(models.Model): # Captura lo que el usuario hace
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	producto = models.ManyToManyField(Producto, blank = True)

	def __str__(self):
		return self.user.username

class post_save_profile_create(sender, instance, created, *args, **kwargs):
	if created:
		Perfil.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
