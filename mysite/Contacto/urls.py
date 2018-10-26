"""
Created by Framework
This file is where you can set the urls to your views.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# Declare the app name
app_name = 'Contacto'
# Declare the url patterns
urlpatterns = [
    # ex: /polls/
    path('contacto/', views.contactanos, name='contacto'),
]

# If the debug setting is on
if settings.DEBUG:
    # Add the patterns of the images
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
