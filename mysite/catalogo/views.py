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
# from Catalogo.models import UserSession
from rest_framework.views import APIView
from rest_framework.response import Response
from Catalogo.filters import *

from django.contrib import messages

# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from Catalogo.forms import *


import json

import re



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
        total = int(quantity) * float(producto.precio)
        # total_cart = request.session.get('total', 0)
        print('Quantity('+ str(quantity) +') * Price('+ str(producto.precio) +') = ' + str(total))
        cart[producto.nombre] = total # quantity.... Quantity of one by the moment
        request.session['cart'] = cart


        # Dictionary made in order to store product with it's quantity
        quantity_dict = request.session.get('quantity_dict', {})
        quantity_dict[producto.nombre] = quantity
        request.session['quantity_dict'] = quantity_dict

        # print(cart[productoid])

        print('Item has been added to the cart')
        # for key, value in cart.items():

        # total_cart += value

        # request.session['total'] = total_cart

        # total = float(request.session.get('total_cart', re('"', '')))
        # total = total + (float(producto.precio) * int(quantity))  # quantity.... Quantity of one by the moment
        # request.session['total_cart'] = total
        # print('Total in cart is currently of: ' + total)

        # for item in cart:
            # print (item)
        print('Item with total: $'+str(cart[producto.nombre]))
        print('Quantity: ' +str(quantity_dict[producto.nombre]))
            # for y in cart[item]: # y = quantity, should print 1
            #     print (y+':'+cart[item][y]) # Print the current cart
        # print('Item:'+cart[productoid]+' has been added to the Cart')
        # productname = get_object_or_404(Producto, nombre)
    # except:
    #     raise Http404("El producto no existe")
    # return HttpResponse("Este es el Producto %s." % productoid)
    return render(request, 'Catalogo/productoinfo.html', {'producto': producto})

# This functions basically calls all of the items stored in the session alongside the quantity of the product
def viewCart(request):
    cart = request.session.get('cart', {})
    quantity_dict = request.session.get('quantity_dict', {})
    request.session['total'] = sum(cart.values())

    entry_dict = {
        "cart":cart,
        "quantity_dict":quantity_dict
    }

    #just declare another dictionary inside the if

    # for item in cart:
    #     print (item)
    if request.method == 'POST':
        # boton = request.POST.get('boton'+item)
        for item, price in cart.items():
            # print(item)
            if request.POST.get('boton'+item):
                
                

                boton = request.POST.get('boton'+item)
                print(item+' button has been pressed')
                # item_to_remove = cart[item]
                # del item_to_remove
                # cart.pop(item)
                # del cart[item]

                # new_total = request.session.get('total')

                # new_total -= float(price)

                # print('New TOTAL: $' + str(new_total))

                # request.session['total'] = 0


                new_cart = removefromCart(cart, item)

                # cart = new_cart # Equivalent line is below
                request.session['cart'] = new_cart

                # Uses same function in order to remove from both dictionaries
                new_quantity_dict = removefromCart(quantity_dict, item)
                request.session['quantity_dict'] = new_quantity_dict

                prev_val = sum(cart.values())
                print('Previous Total: $' + str(prev_val))

                request.session['total'] = sum(new_cart.values())

                new_val = sum(new_cart.values())

                print('New total: $' + str(new_val))

                print('The product '+item+' has been removed from the Cart')

                new_entry_dict = {
                    "cart":new_cart,
                    "quantity_dict":quantity_dict
                }

                cart = new_cart
                return render(request, 'Catalogo/shoppingcart.html', context = new_entry_dict)
        # print('Button pressed was: '+boton)
        # if request.POST.get('checkout'):
            # print('Se presiono ir a checkout')
            # return render(request, 'Catalogo/checkout.html', {'cart':cart})
    # else:
    return render(request, 'Catalogo/shoppingcart.html', context = entry_dict)
    # return HttpResponse("Este es el carrito %s." % json.dumps(cart))
        # for y in cart[item]: # y = quantity, should print 1
            # print (y,':',cart[item][y]) # Print the current cart


    # {'cart':cart}
    # {'cart':new_cart}


# This function removes the item from the cart
def removefromCart(cart, key):
    new_cart = dict(cart)
    del new_cart[key]
    return new_cart



def checkout(request):
    cart = request.session.get('cart', {})
    quantity_dict = request.session.get('quantity_dict', {})
    # total = request.session.total

    for product_name in cart: # y = quantity, should print 1
        print (product_name,':',cart[product_name]) # Print the current cart

    form = OrderForm()
    # order = Ordenes.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_form = Ordenes()

            # product_checkout = ProductosCheckout()

            order_form.nombre = request.POST.get('nombre')
            order_form.correo = request.POST.get('correo')
            print('SESSION TOTAL: '+str(request.session.get('total')))
            order_form.monto_totalcompra = request.session.get('total')
           
            order_form.save() # You can’t associate it with a ProductosCheckout until it’s been saved:
            
            #possible way of iterating and inserting in database the products with their respective quantities and totals
            for product_name in cart: 

                print('The first for has been entered for: '+product_name)
                
                product_checkout = ProductosCheckout()

                product_checkout.nombre_producto = product_name
                product_checkout.total = cart[product_name]
                # product_checkout.save()

                print('Printing NAME ('+product_name+') AND PRICE: '+str(cart[product_name]))

                for name_quant in quantity_dict: 
                    print('Entering quantity for... ')
                    print('name_quant: '+name_quant+' DICT: '+str(quantity_dict[name_quant])+' CART::::::'+product_name+'AND PRICE: '+str(cart[product_name]))
                    print('CHECK THIS OUT... TESTSFOR THE CONDITION')
                    print('name_quant: ('+str(name_quant)+') and product_name: ('+str(product_name)+')')
                    print(name_quant == product_name)

                    if name_quant == product_name:
                        print('THE FINAL IF HAS BEEN ENTERED')
                        print('Printing NAME ('+name_quant+') AND Quantity: '+str(quantity_dict[name_quant]))
                        product_checkout.cantidad = quantity_dict[name_quant]
                        product_checkout.save()
                        order_form.productos.add(product_checkout)
                        print('Product has been added to ORDER')
                        # product_checkout.save() # end of product

            # order_form.cantidad = request.session.

            # order_form.productos = cart
            order_form.save()
            # print(order_form.nombre,order_form.mensaje, json.dumps(cart))
            
            # messages.success(request, 'Tu mensaje ha sido enviado.')
            return HttpResponseRedirect('')
        else:
            form = OrderForm()
    # if len(order)>=1:
    #     order = order[0]

    entry_dict = {
        "form":form,
        # "order":order,
        "cart":cart,
        "quantity_dict":quantity_dict
    }
    return render(request, 'Catalogo/checkout.html', context = entry_dict )


# # This function makes all of the checkout process
# def checkout():
    
#     if request.method == 'POST'
#         form = OrderForm() # Client Information
#         if form.is_valid():
#             # cart_order = Order()
#             # cart_order.numero_referencia  # Aqui se debe de generar un numero aleatorio de alrededor de 15 caracteres
#             cart_order.nombre = request.POST.get('nombre')
#             cart_order.correo = request.POST.get('correo')
#             cart_order.telefono = request.POST.get('telefono')
#             # This saves the order to the database
#             cart_order.save()
#             messages.success(request, 'Tu orden ha sido solicitada, tu numero de referencia es: '+cart_order.numero_referencia+'. Alguien de la organizacion se pondra en contacto con '+cart_order.correo)
#             return HttpResponseRedirect('')
#     else:
#         # Declare a new object for the form of Order
#         form = OrderForm() # Client Information

#     entry_dict = {
#     "form":form }

#     # Render Checkout site
#     return render(request, 'Catalogo/checkout.html',context=entry_dict)









# Falta poder llamar por medio de un post a poder borrar el producto de un carrito

# def removefromCart(request, product):
#     product_id = str(product.id)
#     if product_id in self.cart:
#         # Subtract 1 from the quantity
#         self.cart[product_id]['quantity'] -= 1
#         # If the quantity is now 0, then delete the item
#         if self.cart[product_id]['quantity'] == 0:
#             del self.cart[product_id]
#     return HttpResponse("Este es el carrito")


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
