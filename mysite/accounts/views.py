from django.shortcuts import render

# Create your views here.

from shopping_cart.models import *
from .models import Perfil


def my_profile(request):
	my_user_profile = Perfil.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {'my_orders' : my_orders}

	return render(request, "perfil.html", context)

