"""
Created by Framework
This file is where you can set the urls to your views.
Modified by: Jorge Nino
Date: 19/10/18
"""

# Import the libraries used.
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# Set the name of the app
app_name = 'Actividades'
# Declare the url patterns for each view.
urlpatterns = [
    # ex: /polls/
    path('actividades2/', views.noticias, name='actividades2'),
    path('actividades/', views.noticiasFilter.as_view(), name='actividades'),
    path('AJAXSearchAct/', views.AJAXSearchAct, name='ajaxSearchAct'),
    path('search-submit/', views.SearchSubmitView.as_view(), name='search-submit'),
    path('search-ajax-submit/', views.SearchAjaxSubmitView.as_view(), name='search-ajax-submit'),
]

# if debug is on show images through their url.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
