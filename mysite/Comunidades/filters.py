"""
Created by Framework
This file is where you can create filters to search for data in the website.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries used.
import django_filters as filters
from django_filters import DateRangeFilter,DateFilter
from Comunidades.models import *

# Declare filter class for a model.
class ComunidadFilter(filters.FilterSet):
    # Declare variables that save the columns that will be searched.
    nombre = filters.CharFilter(lookup_expr='icontains')
    descripcion = filters.CharFilter(lookup_expr='icontains')
    # Class to change super Class attributes/configuration
    class Meta:
        model = Comunidad
        fields = ['nombre', 'descripcion']
    # Class creator
    def __init__(self, *args, **kwargs):
        super(ComunidadFilter, self).__init__(*args, **kwargs)
        self.filters['nombre'].label="Nombre de la Comunidad"
        self.filters['descripcion'].label="Descripcion de la Comunidad"
