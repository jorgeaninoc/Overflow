from django.urls import path
from . import views

app_name = 'catalogo'
urlpatterns = [
    # ex: /polls/
    path('',views.catalogo,name='catalogo'),

]

