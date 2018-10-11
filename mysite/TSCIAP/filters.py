import django_filters as filters
from django_filters import DateRangeFilter,DateFilter
from TSCIAP.models import *





class NoticiaFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    texto = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Noticia
        fields = ['titulo', 'texto', 'comunidad', ]
    def __init__(self, *args, **kwargs):
        super(NoticiaFilter, self).__init__(*args, **kwargs)
        self.filters['titulo'].label="Título del Artículo"
        self.filters['texto'].label="Texto"
        self.filters['comunidad'].label="Comunidad Relacionada"



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
