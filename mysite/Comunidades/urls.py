"""
Created by Framework
This file is where the urls of Comunidades are declared for search and for consulting the site.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import the libraries used
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# Declare the app name
app_name = 'Comunidades'

# Declare the url patterns
urlpatterns = [
    # ex: /polls/

    path('search-submit/', views.SearchSubmitView.as_view(), name='search-submit'),
    path('search-ajax-submit/', views.SearchAjaxSubmitView.as_view(), name='search-ajax-submit'),

    path('comunidades/', views.comunidades, name='comunidades'),
    path('AJAXSearch/', views.AJAXSearch, name='ajaxSearch'),
    path('comunidades2/', views.comunidadesFilter.as_view(), name='comunidades2'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
