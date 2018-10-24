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


def noticias(request):
    news_list = Noticia.objects.all()
    paginator = Paginator(news_list,3)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    entry_dict = {"news": news}
    return render(request,'Actividades/noticias.html',context=entry_dict)


class noticiasFilter(ListView):
    model = Noticia
    template_name = 'noticiasFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NoticiaFilter(self.request.GET, queryset=self.get_queryset())
        return context



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
