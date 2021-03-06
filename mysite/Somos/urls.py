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


# Set the name of the app
app_name = 'Somos'

# Declare the url patterns of the app views
urlpatterns = [
    # ex: /polls/
    path('quiensomos/', views.quiensomos, name='quiensomos'),
]
