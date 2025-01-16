from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from products.models import Producto


def home(request):
    pagename = "TIENDA"
    products = Producto.objects.all()
    categories = []

    for product in products:
        if product.categoria not in categories:
            categories.append(product.categoria)

    context = {'title':"Caja", 'pagename':pagename, 'products':products, 'categories':categories}
    return render(request, "abuemp/home.html", context)

