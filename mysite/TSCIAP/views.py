from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from TSCIAP.models import Community, Notice, Image, Product, Video, IndexImage

# Create your views here.
def index(request):
    """
    To add a video copy the embedded link and add it (ONLY EMBEDDED LINK)
    """
    vid_list = Video.objects.all()
    entry_dict = {"videos":vid_list[0].url.replace('watch?v=','embed/')}
    print(str(vid_list[0]))
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
