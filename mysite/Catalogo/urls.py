from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'Catalogo'
urlpatterns = [
    # ex: /polls/

    path('search-submit/', views.SearchSubmitView.as_view(), name='search-submit'),
    path('search-ajax-submit/', views.SearchAjaxSubmitView.as_view(), name='search-ajax-submit'),

    path('catalogo/',views.catalogo,name='catalogo'),
    path('catalogoFilter/', views.catalogoFilter.as_view(),name='catalogoFilter'),
    path('catalogo/<int:productoid>/', views.getProducto, name='producto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
