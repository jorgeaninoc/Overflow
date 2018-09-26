from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from TSCIAP.models import Comunidad, Noticia, Imagen, Producto, Video, InicioImagen, GaleriaImagen

# Create your views here.
def index(request):
    vid_list = Video.objects.all()
    if len(vid_list) > 0:
        vid_list = vid_list[0].url.replace('watch?v=','embed/')
    else:
        vid_list = None

    indeximg = InicioImagen.objects.all()
    if len(indeximg) > 0:
        indeximg = indeximg[0]
    else:
        indeximg = None

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
    if len(news_list) == 0:
        news_list = None
    entry_dict = {"news": news_list}
    return render(request,'TSCIAP/noticias.html',context=entry_dict)


def quiensomos(request):
	return render(request, 'TSCIAP/quiensomos.html');

def comunidades(request):
	return render(request, 'TSCIAP/comunidades.html');

def colabora(request):
	return render(request, 'TSCIAP/colabora.html');

def contactanos(request):
	return render(request, 'TSCIAP/contactinformation.html');

def catalogo(request):
	return render(request, 'TSCIAP/catalogo.html');
