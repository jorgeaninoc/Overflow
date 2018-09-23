from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'TSCIAP/index.html')

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
