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
from Inicio.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from Comunidades.models import Imagen
from Catalogo.models import Producto
# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    vid_list = Video.objects.all()
    indeximg = InicioImagen.objects.all()
    products_list = Producto.objects.all()
    galery_list = GaleriaImagen.objects.all()
    announces_list = Anuncio.objects.all()

    if len(vid_list) > 0:
        vid_list = vid_list[0].url.replace('watch?v=','embed/')
    else:
        vid_list = None

    images_list = []

    if len(products_list) >= 3:
        products_list = products_list[:3]

    for i in products_list:
        if len(i.imagenes.all())>0:
            images_list.append(i.imagenes.all()[0])

    if len(galery_list) >= 6:
        galery_list = galery_list[:6]
    else:
        if len(galery_list) == 0:
            img_list = Imagen.objects.all()
            if len(img_list) >= 6:
                galery_list = img_list[:6]
            else:
                galery_list = img_list

    if len(announces_list) >= 1:
        announces_list = announces_list[0]

    print(products_list[0].imagenes)

    entry_dict = {
    "videos": vid_list,
    "products":products_list,
    "products_images":images_list,
    "indeximages" : indeximg,
    "galeryimages": galery_list,
    "announces":announces_list}
    return render(request,'Inicio/index.html',context=entry_dict)



class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})

def get_data(request, *args, **kwargs):
    queryset = Foo.objects.all()
    dates = [obj.created for obj in queryset]
    counts = [obj.amount for obj in queryset]
    context = {
        'dates': json.dumps(dates),
        'counts': json.dumps(counts),
    }

    return render(request, template, context)#Jsonn Response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
         data = {
            "sales": 100,
            "customers":10,
        }
         return Response(data)
