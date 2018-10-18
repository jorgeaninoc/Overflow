from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'Actividades'
urlpatterns = [
    # ex: /polls/
    path('noticias/', views.noticias, name='noticias'),
    path('noticiasFilter/', views.noticiasFilter.as_view(), name='noticiasFilter'),

    path('search-submit/', views.SearchSubmitView.as_view(), name='search-submit'),
    path('search-ajax-submit/', views.SearchAjaxSubmitView.as_view(), name='search-ajax-submit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
