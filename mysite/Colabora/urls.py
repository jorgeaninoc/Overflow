"""
Created by Framework
This file is where the urls of Colabora are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'Colabora'
urlpatterns = [
    # ex: /polls/
    path('colabora/', views.colabora, name='colabora'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
