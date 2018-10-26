from django.shortcuts import render
from django.views.generic import View
from django.template import loader
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from Contacto.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from Contacto.forms import *
from django.contrib import messages

# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
def contactanos(request):
    form = MensajeForm()
    contacto = Contacto.objects.all()

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            m = Mensaje()
            m.nombre = request.POST.get('nombre')
            m.correo = request.POST.get('correo')
            m.mensaje = request.POST.get('mensaje')
            print(m.nombre,m.mensaje,m.correo)
            m.save()
            messages.success(request, 'Tu mensaje ha sido enviado.')
            return HttpResponseRedirect('')
        else:
            form = MensajeForm()
    if len(contacto)>=1:
        contacto = contacto[0]

    entry_dict = {
        "form":form,
        "contacto":contacto
    }
    return render(request, 'Contacto/contactinformation.html',context=entry_dict)
