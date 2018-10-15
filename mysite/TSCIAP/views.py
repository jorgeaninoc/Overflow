from django.shortcuts import render
from django.views.generic import View
from django.template import loader
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from TSCIAP.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from TSCIAP.forms import *
from TSCIAP.filters import *

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

    entry_dict = {
    "videos": vid_list,
    "products":products_list,
    "products_images":images_list,
    "indeximages" : indeximg,
    "galeryimages": galery_list,
    "announces":announces_list}
    return render(request,'TSCIAP/index.html',context=entry_dict)

def noticias(request):
    news_list = Noticia.objects.all()
    paginator = Paginator(news_list,3)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    entry_dict = {"news": news}
    return render(request,'TSCIAP/noticias.html',context=entry_dict)


class noticiasFilter(ListView):
    model = Noticia
    template_name = 'TSCIAP/noticiasFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NoticiaFilter(self.request.GET, queryset=self.get_queryset())
        return context



class SearchSubmitView(View):
    template = 'TSCIAP/search_submit.html'
    """
    template = 'TSCIAP/search_results.html'
    """
    response_message = 'This is the response'

    def post(self, request):
        template = loader.get_template(self.template)
        query = request.POST.get('search', '')

        # A simple query for Item objects whose title contain 'query'
        items = Noticia.objects.filter(titulo__icontains=query)

        context = {'title': self.response_message, 'query': query, 'items': items}

        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template, content_type='text/html')

class SearchAjaxSubmitView(SearchSubmitView):
    template = 'TSCIAP/search_results.html'
    response_message = 'This is the AJAX response'




def catalogo(request):
    product_list = Producto.objects.all()
    paginator = Paginator(product_list,9)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    entry_dict = {"products":products}

    return render(request,'TSCIAP/catalogo.html',context=entry_dict)



class catalogoFilter(ListView):
    model = Producto
    template_name = 'TSCIAP/catalogoFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CatalogoFilter(self.request.GET, queryset=self.get_queryset())
        return context



def getProducto(request, productoid):
    try:
        producto = get_object_or_404(Producto, pk=productoid)
        # productname = get_object_or_404(Producto, nombre)
    except:
        raise Http404("Producto does not exist")
    # return HttpResponse("Este es el Producto %s." % productoid)
    return render(request, 'TSCIAP/productoinfo.html', {'producto': producto})

def comunidades(request):
    communities_list = Comunidad.objects.all()
    paginator=Paginator(communities_list,3)
    page = request.GET.get("page")
    communities = paginator.get_page(page)
    entry_dict = {
    "communities":communities
    }
    return render(request,'TSCIAP/comunidades.html',context=entry_dict)


class comunidadesFilter(ListView):
    model = Comunidad
    template_name = 'TSCIAP/comunidadesFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ComunidadFilter(self.request.GET, queryset=self.get_queryset())
        return context







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
    return render(request, 'TSCIAP/colabora.html',context=entry_dict)

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
            return HttpResponseRedirect('')
        else:
            form = MensajeForm()
    if len(contacto)>=1:
        contacto = contacto[0]

    entry_dict = {
        "form":form,
        "contacto":contacto
    }
    return render(request, 'TSCIAP/contactinformation.html',context=entry_dict)


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
