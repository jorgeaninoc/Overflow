from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'Inicio'
urlpatterns = [
    path('',views.index,name='index'),
    path('api/',views.ChartView.as_view(),name='charts'),
    path('api/data/',views.get_data,name='get_data'),
    path('api/chart/data/',views.ChartData.as_view(),name='chart_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
