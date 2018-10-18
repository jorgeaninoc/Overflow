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



class SearchSubmitView(View):
    template = 'TSCIAP/search_submit.html'
    """
    template = 'TSCIAP/search_results.html'
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




def comunidades(request):
    communities_list = Comunidad.objects.all()
    paginator=Paginator(communities_list,3)
    page = request.GET.get("page")
    communities = paginator.get_page(page)
    entry_dict = {
    "communities":communities
    }
    return render(request,'Comunidades/comunidades.html',context=entry_dict)


class comunidadesFilter(ListView):
    model = Comunidad
    template_name = 'Comunidades/comunidadesFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ComunidadFilter(self.request.GET, queryset=self.get_queryset())
        return context
