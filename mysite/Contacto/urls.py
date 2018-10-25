from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'Contacto'
urlpatterns = [
    # ex: /polls/
    path('contacto/', views.contactanos, name='contacto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
