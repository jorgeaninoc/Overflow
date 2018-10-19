"""
Created by Framework
This file is where the views of Comunidades are declared, and where the search/filter
views are called.
Modified by: Jorge Nino
Date: 19/10/18
"""
# Import libraries needed
from django.shortcuts import render
from django.views.generic import View
from django.template import loader
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from Comunidades.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from Comunidades.filters import *

# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404



# Declare class to search/filter communities
class SearchSubmitView(View):
    # Set the url to submit the search
    template = 'Comunidades/search_submit.html'
    # Declare a response message
    response_message = 'This is the response'

    # Crete post function to retrieve the template of the submission
    def post(self, request):
        # Get the template
        template = loader.get_template(self.template)
        # Get the search result from the POST object
        query = request.POST.get('search', '')

        # A simple query for Item objects whose title contain 'query'
        items = Noticia.objects.filter(titulo__icontains=query)

        # Declare dictionary with info that is going to be sent to the html
        context = {'title': self.response_message, 'query': query, 'items': items}

        # Save the rendered template
        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template, content_type='text/html')

class SearchAjaxSubmitView(SearchSubmitView):
    template = 'search_results.html'
    response_message = 'This is the AJAX response'

# Declare function for showing communities in the url
def comunidades(request):
    # Get all the objects from the communities model
    communities_list = Comunidad.objects.all()
    # Create a paginator that accepts 3 communities for each page
    paginator=Paginator(communities_list,3)
    # Get the page where the pagination is going to be added using GET
    page = request.GET.get("page")
    # Get the paginator applied to the page
    communities = paginator.get_page(page)
    # Declare the dictionary that is going to be passed to the html
    entry_dict = {
    "communities":communities
    }
    # Render the site with the elements in the dictionary
    return render(request,'Comunidades/comunidades.html',context=entry_dict)


class comunidadesFilter(ListView):
    model = Comunidad
    template_name = 'Comunidades/comunidadesFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ComunidadFilter(self.request.GET, queryset=self.get_queryset())
        return context