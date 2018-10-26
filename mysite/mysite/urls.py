"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
Created by Framework
This file is where all the urls from the apps are set
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('Inicio.urls')),
    path('',include('Comunidades.urls')),
    path('',include('Catalogo.urls')),
    path('',include('Somos.urls')),
    path('',include('Contacto.urls')),
    path('',include('Actividades.urls')),
    path('',include('Colabora.urls')),
    path('admin/', admin.site.urls),
]
