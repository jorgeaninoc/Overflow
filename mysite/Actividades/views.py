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
from Actividades.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from Actividades.filters import *

# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


# Declare the view for accesing the Actividades.
def noticias(request):
    # Get all the Notice objects from the DB
    news_list = Noticia.objects.all()
    # Set a paginator of 3 objects.
    paginator = Paginator(news_list,3)
    # Get the site.
    page = request.GET.get('page')
    # Set the paginator to the site.
    news = paginator.get_page(page)
    # Declare the dict with the data that will be used in the view.
    entry_dict = {"news": news}
    # Render the site.
    return render(request,'Actividades/noticias.html',context=entry_dict)


# This function filters the data of a Notice.
class noticiasFilter(ListView):
    model = Noticia
    template_name = 'Actividades/noticiasFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NoticiaFilter(self.request.GET, queryset=self.get_queryset())
        return context


# This function searches for the data of a Notice when submitted
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
