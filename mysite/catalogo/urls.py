"""
Created by Framework
This file is where you can set the urls to your views.
Modified by: Jorge Nino
Date: 19/10/18
"""

# Import libraries used
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# Set the name of the app
app_name = 'Catalogo'
# Declare the url patterns for each view.
urlpatterns = [
    # ex: /polls/

    path('search-submit/', views.SearchSubmitView.as_view(), name='search-submit'),
    path('search-ajax-submit/', views.SearchAjaxSubmitView.as_view(), name='search-ajax-submit'),

    path('catalogo2/',views.catalogo,name='catalogo2'),

    path('catalogo/', views.catalogoFilter.as_view(),name='catalogo'),
    path('catalogo/<int:productoid>/', views.getProducto, name='producto'),
    path('carrito/', views.viewCart, name='carrito'),
    path('checkout/', views.checkout, name = 'checkout'),
]
# if debug is on show images through their url.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
