from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def catalogo(request):
	return render(request, 'catalogo/catalogo.html');