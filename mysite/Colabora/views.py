"""
Created by Framework
This file is where the views of Colabora are declared, and where the search/filter
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
from Colabora.models import *
from rest_framework.views import APIView
from Colabora.forms import *
from rest_framework.response import Response

# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


# Declare function for showing colabora site
def colabora(request):
    # Create the form that will be filled by the user to offer colaboration
    form = ColaboradorForm()
    # Get all the ColaboraImagen objects from the db
    icolab = ColaboraImagen.objects.all()

    # If the form is submitted
    if request.method == 'POST':
        # Get the info filled in the form of the Colabora site
        form = ColaboradorForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # If the form is valid create an object of the model Colaborador
            c = Colaborador()
            # Set the attributed of the Colaborador object according to the form
            c.nombre = request.POST.get('nombre')
            c.telefono = request.POST.get('telefono')
            c.correo = request.POST.get('correo')
            c.empresa = request.POST.get('empresa')
            # Save the object to the db
            c.save()
            # Reload the site
            return HttpResponseRedirect('')
    else:
        # Declare a new object for the form of Colabora
        form = ColaboradorForm()

    # If theres more than one Image for Colabora site, get the last one uploaded
    if len(icolab) >= 1:
        icolab = icolab[0]

    # Declare the dict that will be sent to the Colabora site
    entry_dict = {
    "form":form,
    "icolab":icolab
    }
    # Render Colabora site
    return render(request, 'Colabora/colabora.html',context=entry_dict)
