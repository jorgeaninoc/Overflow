from django.contrib import admin
from TSCIAP.models import Comunidad, Imagen, Producto, Noticia, Video, InicioImagen, GaleriaImagen

# Register your models here.
admin.site.register(Comunidad)
admin.site.register(Imagen)
admin.site.register(Producto)
admin.site.register(Noticia)
admin.site.register(Video)
admin.site.register(GaleriaImagen)
admin.site.register(InicioImagen)
