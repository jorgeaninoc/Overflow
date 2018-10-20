"""
Created by Framework
This file is where the urls of Colabora are declared.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import the libraries used
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



# Declare the app name
app_name = 'Colabora'
# Declare the url patterns
urlpatterns = [
    # ex: /polls/
    # Set the path to the view and the name of the window
    path('colabora/', views.colabora, name='colabora'),
]

# If the debug setting is on
if settings.DEBUG:
    # Add the patterns of the images
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
