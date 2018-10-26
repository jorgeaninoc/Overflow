"""
Created by Framework
This file is where you can create views for the App
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import the libraries used.
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




# This function searches for the data of a Product when submitted
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



# Declare the view for accesing the Catalogo site.
def catalogo(request):
    # Get all the objects of Product from the DB.
    product_list = Producto.objects.all()
    # Set a paginator of 9 objects.
    paginator = Paginator(product_list,9)
    # Get the site of the view.
    page = request.GET.get('page')
    # Set the paginator to the site.
    products = paginator.get_page(page)
    # Declare a dict with the data passed to the view.
    entry_dict = {"products":products}
    # Render the view.
    return render(request,'Catalogo/catalogo.html',context=entry_dict)


# This function filters the data of a Product.
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
