"""
Created by Framework
This file is where you can create views for the App
Modified by: Enrique Posada
Date: 03/11/18
"""
# Import the libraries used.
from django.shortcuts import render
from django.views.generic import View
from django.template import loader
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from Catalogo.models import *
from Catalogo.models import UserSession
from rest_framework.views import APIView
from rest_framework.response import Response
from Catalogo.filters import *

# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


import json



# This function searches for the data of a Product when submitted
class SearchSubmitView(View):
    template = 'search_submit.html'
    """
    template = 'search_results.html'
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
    template = 'search_results.html'
    response_message = 'This is the AJAX response'



# Declare the view for accesing the Catalogo site.
def catalogo(request):
    # Get all the objects of Product from the DB.
    product_list = Producto.objects.all()
    # Set a paginator of 9 objects.
    paginator = Paginator(product_list,9)
    # Get the site of the view.
    page = request.GET.get('page')
    # Set the paginator to the site.
    products = paginator.get_page(page)
    # Declare a dict with the data passed to the view.
    entry_dict = {"products":products}
    # Render the view.
    return render(request,'Catalogo/catalogo.html',context=entry_dict)


# This function filters the data of a Product.
class catalogoFilter(ListView):
    model = Producto
    template_name = 'Catalogo/catalogoFilter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CatalogoFilter(self.request.GET, queryset=self.get_queryset())
        return context



def getProducto(request, productoid):
    # try:
    producto = get_object_or_404(Producto, pk=productoid)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        cart = request.session.get('cart', {})
        cart[productoid] = quantity  # quantity.... Quantity of one by the moment
        request.session['cart'] = cart
        # print(cart[productoid])
        print('Item has been added to the cart')
        # for item in cart:
            # print (item)
            # for y in cart[item]: # y = quantity, should print 1
                # print (y,':',cart[items][y]) # Print the current cart
        # print('Item:'+cart[productoid]+' has been added to the Cart')
        # productname = get_object_or_404(Producto, nombre)
    # except:
    #     raise Http404("El producto no existe")
    # return HttpResponse("Este es el Producto %s." % productoid)
    return render(request, 'Catalogo/productoinfo.html', {'producto': producto})

# This functions basically calls all of the items stored in the session alongside the quantity of the product
def viewCart(request):
    cart = request.session.get('cart', {})
    # for item in cart:
    #     print (item)
    return render(request, 'Catalogo/shoppingcart.html', {'cart':cart})
    # return HttpResponse("Este es el carrito %s." % json.dumps(cart))
        # for y in cart[item]: # y = quantity, should print 1
            # print (y,':',cart[item][y]) # Print the current cart


# Falta poder llamar por medio de un post a poder borrar el producto de un carrito

def removefromCart(request, product):
    product_id = str(product.id)
    if product_id in self.cart:
        # Subtract 1 from the quantity
        self.cart[product_id]['quantity'] -= 1
        # If the quantity is now 0, then delete the item
        if self.cart[product_id]['quantity'] == 0:
            del self.cart[product_id]
    return HttpResponse("Este es el carrito")


    # print('Here is the content of the cart'+cart)

# def addCart(request, item_id, quantity):
#     cart = request.session.get('cart', {})
#     cart[item_id] = quantity
#     request.session['cart'] = cart


# def getCarrito(request):
    
#     if not request.session.session_key:
#         request.session.create()

#     print('Session KEY is: '+request.session.session_key)
#     # user = get_object_or_404(UserSession, user=request.session.session_key)
#     """ This view displays what is in a user's cart. """
#     # Based on the user who is making the request, grab the cart object
#     # my_cart = Cart.objects.get(user=0)
#     if my_cart == 0:
#         print('THE CART OF THE USER IS EMPTY')
#     else:
#     # Get a queryset of entries that correspond to "my_cart"
#         list_of_entries = Entry.objects.filter(cart=my_cart)
#         # Make a list of the product's names
#         list_of_products = list(list_of_entries.values_list('product__name', flat=True))
#         # Remove redundant product names
#         list_of_products = list(set(list_of_products))
#     return render(request, 'shoppingcart.html', {'list_of_products': list_of_products})
#     #return HttpResponse("Este es el Carrito %s.", % list_of_products: list_of_products)
