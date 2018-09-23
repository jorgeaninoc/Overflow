from django.urls import path
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
