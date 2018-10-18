import django_filters as filters
from django_filters import DateRangeFilter,DateFilter
from Comunidades.models import *

class ComunidadFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    descripcion = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Comunidad
        fields = ['nombre', 'descripcion']
    def __init__(self, *args, **kwargs):
        super(ComunidadFilter, self).__init__(*args, **kwargs)
        self.filters['nombre'].label="Nombre de la Comunidad"
        self.filters['descripcion'].label="Descripcion de la Comunidad"
