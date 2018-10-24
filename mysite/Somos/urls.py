from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'Somos'
urlpatterns = [
    # ex: /polls/
    path('quiensomos/', views.quiensomos, name='quiensomos'),
]
