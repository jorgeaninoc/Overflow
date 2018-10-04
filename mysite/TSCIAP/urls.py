from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'TSCIAP'
urlpatterns = [
    # ex: /polls/
    
    path('',views.index,name='index'),
    path('quiensomos/', views.quiensomos, name='quiensomos'),
    path('noticias/', views.noticias, name='noticias'),
    path('comunidades/', views.comunidades, name='comunidades'),
    path('colabora/', views.colabora, name='colabora'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('catalogo/',views.catalogo,name='catalogo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
