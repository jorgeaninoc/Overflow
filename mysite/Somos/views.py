"""
Created by Framework
This file is where you can create views for the App
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
from Somos.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from Contacto.models import Contacto





# View for Somos app
def quiensomos(request):
    """
    This function renders the Somos site with the required information
    """
    # Declare the variables used in the site
    somos_list = Somos.objects.all()
    mision_list = Mision.objects.all()
    historia_list = Historia.objects.all()
    valor_list = Valor.objects.all()
    contacto_list = Contacto.objects.all()

    # Conditionals to grab the last object uploaded to the DB.
    if len(somos_list) >= 1:
        somos_list = somos_list[0]
    if len(mision_list) >=1:
        mision_list = mision_list[0]
    if len(historia_list) >=1:
        historia_list = historia_list[0]
    if len(valor_list) >=1:
        valor_list = valor_list[0]
    if len(contacto_list)>=3:
        contacto_list = contacto_list[:3]

    # Declare the context dict with the information used by the site
    entry_dict = {
    "titles":somos_list,
    "misions":mision_list,
    "valores":valor_list,
    "historias":historia_list,
    "contacto":contacto_list
    }

    # Render the site of Somos.
    return render(request, 'Somos/quiensomos.html', context = entry_dict )
