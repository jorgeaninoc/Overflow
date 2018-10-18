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


def colabora(request):
    form = ColaboradorForm()
    icolab = ColaboraImagen.objects.all()

    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            c = Colaborador()
            c.nombre = request.POST.get('nombre')
            c.telefono = request.POST.get('telefono')
            c.correo = request.POST.get('correo')
            c.empresa = request.POST.get('empresa')
            c.save()
            return HttpResponseRedirect('')
    else:
        form = ColaboradorForm()

    if len(icolab) >= 1:
        icolab = icolab[0]

    entry_dict = {
    "form":form,
    "icolab":icolab
    }
    return render(request, 'Colabora/colabora.html',context=entry_dict)
