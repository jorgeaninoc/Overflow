from django.shortcuts import render
from django.views.generic import View
from django.template import loader
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from Catalogo.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from Catalogo.filters import *

# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404





class SearchSubmitView(View):
    template = 'search_submit.html'
    """
    template = 'search_results.html'
    """
    response_message = 'This is the response'

    def post(self, request):
        template = loader.get_template(self.template)
        query = request.POST.get('search', '')

        # A simple query for Item objects whose title contain 'query'
        items = Noticia.objects.filter(titulo__icontains=query)

        context = {'title': self.response_message, 'query': query, 'items': items}

        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template, content_type='text/html')

class SearchAjaxSubmitView(SearchSubmitView):
    template = 'search_results.html'
    response_message = 'This is the AJAX response'




def catalogo(request):
    product_list = Producto.objects.all()
    paginator = Paginator(product_list,9)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    entry_dict = {"products":products}

    return render(request,'Catalogo/catalogo.html',context=entry_dict)



class catalogoFilter(ListView):
    model = Producto
    template_name = 'Catalogo/catalogoFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CatalogoFilter(self.request.GET, queryset=self.get_queryset())
        return context



def getProducto(request, productoid):
    try:
        producto = get_object_or_404(Producto, pk=productoid)
        # productname = get_object_or_404(Producto, nombre)
    except:
        raise Http404("Producto does not exist")
    # return HttpResponse("Este es el Producto %s." % productoid)
    return render(request, 'Catalogo/productoinfo.html', {'producto': producto})
