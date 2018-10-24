from django.shortcuts import render
from django.views.generic import View
from django.template import loader
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from Somos.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404







def quiensomos(request):
    somos_list = Somos.objects.all()
    mision_list = Mision.objects.all()
    historia_list = Historia.objects.all()
    valor_list = Valor.objects.all()


    if len(somos_list) >= 1:
        somos_list = somos_list[0]
    if len(mision_list) >=1:
        mision_list = mision_list[0]
    if len(historia_list) >=1:
        historia_list = historia_list[0]
    if len(valor_list) >=1:
        valor_list = valor_list[0]
    entry_dict = {
    "titles":somos_list,
    "misions":mision_list,
    "valores":valor_list,
    "historias":historia_list
    }


    return render(request, 'Somos/quiensomos.html', context = entry_dict )
