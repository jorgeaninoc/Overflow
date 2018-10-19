"""
Created by Framework
This file is where the urls of Comunidades are declared for search and for consulting the site.
Modified by: Jorge Nino
Date: 19/10/18
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'Comunidades'
urlpatterns = [
    # ex: /polls/

    path('search-submit/', views.SearchSubmitView.as_view(), name='search-submit'),
    path('search-ajax-submit/', views.SearchAjaxSubmitView.as_view(), name='search-ajax-submit'),

    path('comunidades/', views.comunidades, name='comunidades'),
    path('comunidadesFilter/', views.comunidadesFilter.as_view(), name='comunidadesFilter'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
