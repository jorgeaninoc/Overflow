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
from Comunidades.models import *
from Contacto.models import Contacto
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



def AJAXSearchCat(request):
    if(request.POST.get('precio__gt')!= None and request.POST.get('precio__gt')!=''):
        pgt = int(request.POST.get('precio__gt'))
    else:
        pgt = 0

    if(request.POST.get('precio__lt')!= None and request.POST.get('precio__lt')!=''):
        plt = int(request.POST.get('precio__lt'))
    else:
        plt = 999999

    if(request.POST.get('nombre') != None):
        nombre = request.POST.get('nombre')
    else:
        nombre = ''

    if(request.POST.get('comunidad') != None):
        com = request.POST.get('comunidad')
    else:
        com = ''

    coms = Comunidad.objects.filter(nombre__icontains=com)
    result = Producto.objects.filter(nombre__icontains=nombre)
    result = result.filter(communidad__in=coms)
    result = result.filter(precio__gte=pgt)
    result = result.filter(precio__lte=plt)

    return render(request,"Catalogo/cat_results.html", {'result':result})
#    html = render_to_string("/Comunidades/com_results.html", {'result':result})
#    return HttpResponse(html)


# Declare the view for accesing the Catalogo site.
def catalogo(request):
    contacto_list = Contacto.objects.all()
    # Get all the objects of Product from the DB.
    product_list = Producto.objects.all()
    # Set a paginator of 9 objects.
    paginator = Paginator(product_list,9)
    communities = Comunidad.objects.all()
    # Get the site of the view.
    page = request.GET.get('page')
    # Set the paginator to the site.
    products = paginator.get_page(page)
    # Declare a dict with the data passed to the view.
    if len(contacto_list)>=3:
        contacto_list = contacto_list[:3]
    entry_dict = {"products":products, "communities": communities,"contacto":contacto_list}
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
