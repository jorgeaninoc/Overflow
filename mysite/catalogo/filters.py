import django_filters as filters
from django_filters import DateRangeFilter,DateFilter
from Catalogo.models import *
class CatalogoFilter(filters.FilterSet):
    precio = filters.NumberFilter()
    precio__gt = filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio__lt = filters.NumberFilter(field_name='precio', lookup_expr='lte')

    class Meta:
        model = Producto
        fields = ['nombre', 'communidad', 'precio']

    def __init__(self, *args, **kwargs):
        super(CatalogoFilter, self).__init__(*args, **kwargs)
        self.filters['nombre'].label="Nombre del Producto"
        self.filters['precio__gt'].label="Precio mayor o igual a"
        self.filters['precio__lt'].label="Precio menor o igual a"
