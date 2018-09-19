from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'noticias/index.html')

def quiensomos(request):
	return render(request, 'noticias/contactinformation.html');

def noticias(request):
	return render(request, 'noticias/contactinformation.html');

def comunidades(request):
	return render(request, 'noticias/comunidades.html');

def colabora(request):
	return render(request, 'noticias/contactinformation.html');

def catalogo(request):
	return render(request, 'noticias/contactinformation.html');

def contactanos(request):
	return render(request, 'noticias/contactinformation.html');