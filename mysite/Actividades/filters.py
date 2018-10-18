import django_filters as filters
from django_filters import DateRangeFilter,DateFilter
from Actividades.models import *

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
