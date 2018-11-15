"""
Created by Framework
This file is where you can create filters to search for data in the website.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries used.
import django_filters as filters
from django_filters import DateRangeFilter,DateFilter
from Catalogo.models import *

# Declare filter class for a model.
class CatalogoFilter(filters.FilterSet):

    CHOICES = (
        ('ascendente', 'Ascendente'),
        ('descendente', 'Descendente')
    )

    orden = filters.ChoiceFilter(label = 'Ordenar por Precio', choices = CHOICES, method = 'filter_by_order')

    # Declare variables that save the columns that will be searched.
    nombre = filters.CharFilter(lookup_expr='icontains')
    precio = filters.NumberFilter()
    precio__gt = filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio__lt = filters.NumberFilter(field_name='precio', lookup_expr='lte')

    # Class to change super Class attributes/configuration
    class Meta:
        model = Producto
        fields = ['nombre', 'communidad', 'precio']

    # Class creator
    def __init__(self, *args, **kwargs):
        super(CatalogoFilter, self).__init__(*args, **kwargs)
        self.filters['nombre'].label="Nombre del Producto"
        self.filters['precio__gt'].label="Precio mayor o igual a"
        self.filters['precio__lt'].label="Precio menor o igual a"


    def filter_by_order(self, queryset, name, value):
        expression = 'precio' if value == 'ascendente' else '-precio'
        return queryset.order_by(expression)
