from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from TSCIAP.models import *

# Create your views here.
def index(request):
    vid_list = Video.objects.all()
    if len(vid_list) > 0:
        vid_list = vid_list[0].url.replace('watch?v=','embed/')
    else:
        vid_list = None

    indeximg = InicioImagen.objects.all()

    products_list = Producto.objects.all()
    images_list = []

    if len(products_list) >= 3:
        products_list = products_list[:3]

    for i in products_list:
        if len(i.imagenes.all())>0:
            images_list.append(i.imagenes.all()[0])


    galery_list = GaleriaImagen.objects.all()
    if len(galery_list) >= 6:
        galery_list = galery_list[:6]
    else:
        if len(galery_list) == 0:
            img_list = Imagen.objects.all()
            if len(img_list) >= 6:
                galery_list = img_list[:6]
            else:
                galery_list = img_list
    entry_dict = {
    "videos": vid_list,
    "products":products_list,
    "products_images":images_list,
    "indeximages" : indeximg,
    "galeryimages": galery_list}
    return render(request,'TSCIAP/index.html',context=entry_dict)

def noticias(request):
    news_list = Noticia.objects.all()
    paginator = Paginator(news_list,3)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    entry_dict = {"news": news}
    return render(request,'TSCIAP/noticias.html',context=entry_dict)

def catalogo(request):
    product_list = Producto.objects.all()
    paginator = Paginator(product_list,9)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    entry_dict = {"products":products}

    return render(request,'TSCIAP/catalogo.html',context=entry_dict)

def comunidades(request):
    communities_list = Comunidad.objects.all()
    paginator=Paginator(communities_list,3)
    page = request.GET.get("page")
    communities = paginator.get_page(page)
    entry_dict = {
    "communities":communities
    }
    return render(request,'TSCIAP/comunidades.html',context=entry_dict)


def quiensomos(request):
    somos_list = Somos.objects.all()
    mision_list = Mision.objects.all()
    vision_list = Vision.objects.all()
    valor_list = Valor.objects.all()
    politicas_list = Politica.objects.all()


    if len(somos_list) >= 1:
        somos_list = somos_list[0]
    if len(mision_list) >=1:
        mision_list = mision_list[0]
    if len(vision_list) >=1:
        vision_list = vision_list[0]
    if len(valor_list) >=1:
        valor_list = valor_list[0]
    if len(politicas_list) >=1:
        politicas_list = politicas_list[0]

    entry_dict = {
    "titles":somos_list,
    "misions":mision_list,
    "valores":valor_list,
    "visions":vision_list,
    "politics":politicas_list
    }


    return render(request, 'TSCIAP/quiensomos.html', context = entry_dict )


def colabora(request):
    return render(request, 'TSCIAP/colabora.html')

def contactanos(request):
    return render(request, 'TSCIAP/contactinformation.html')
