from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from TSCIAP.models import Community, Notice, Image, Product, Video, IndexImage, GaleryImage

# Create your views here.
def index(request):
    """
    To add a video copy the embedded link and add it (ONLY EMBEDDED LINK)
    """

    if len(Video.objects.all()) > 0:
        vid_list = Video.objects.all()[0].url.replace('watch?v=','embed/')
    else:
        vid_list = None
    indeximg = IndexImage.objects.all()
    if len(Product.objects.all()) >= 3:
        products_list = Product.objects.all()[:3]
    else:
        products_list = Product.objects.all()
    if len(GaleryImage.objects.all()) >= 6:
        galery_list = GaleryImage.objects.all()[:6]
    else:
        if len(GaleryImage.objects.all()) == 0:
            if len(Image.objects.all()) >= 6:
                galery_list = Image.objects.all()[:6]
            else:
                galery_list = Image.objects.all()
        else:
            galery_list  = GaleryImage.objects.all()
    entry_dict = {"videos":vid_list,
    "products":products_list,
    "indeximages" : indeximg,
    "galeryimages": galery_list}
    return render(request,'TSCIAP/index.html',context=entry_dict)

def noticias(request):
	return render(request, 'TSCIAP/noticias.html');

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
