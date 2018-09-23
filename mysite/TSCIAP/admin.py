from django.contrib import admin
from TSCIAP.models import Community, Image, Product, Notice, Video, IndexImage, GaleryImage

# Register your models here.
admin.site.register(Community)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Notice)
admin.site.register(Video)
admin.site.register(GaleryImage)
admin.site.register(IndexImage)
