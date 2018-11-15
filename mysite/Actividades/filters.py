"""
Created by Framework
This file is where you can create filters to search for data in the website.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries that will be used.
import django_filters as filters
from django_filters import DateRangeFilter,DateFilter
from Actividades.models import *

# Declare filter class for a model.
class NoticiaFilter(filters.FilterSet):

    CHOICES = (
        ('ascendente', 'Más Recientes Primero'),
        ('descendente', 'Más Antiguos Primero')
    )

    orden = filters.ChoiceFilter(label = 'Orden', choices = CHOICES, method = 'filter_by_order')
    # Declare variables that save the columns that will be searched.
    titulo = filters.CharFilter(lookup_expr='icontains')
    texto = filters.CharFilter(lookup_expr='icontains')


    # Class to change super Class attributes/configuration
    class Meta:
        model = Noticia
        fields = ['titulo', 'texto', 'comunidad', ]
    def __init__(self, *args, **kwargs):
        super(NoticiaFilter, self).__init__(*args, **kwargs)
        self.filters['titulo'].label="Título del Artículo"
        self.filters['texto'].label="Texto"
        self.filters['comunidad'].label="Comunidad Relacionada"
    def filter_by_order(self, queryset, name, value):
        expression = 'fechaInicio' if value == 'ascendente' else '-fechaInicio'
        return queryset.order_by(expression)
