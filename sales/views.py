import os
import pandas as pd
import sqlite3 as sql3
import pandas as pd
from datetime import datetime, timedelta
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from dbs.dbs import recordDb
from products.models import Producto
from abuemp.decorators import admin_only
from .models import BasketDb
from .forms import CreateSalesForm
from .basket import Basket


@admin_only
def sales(request):
    pagename = "VENTAS"
    lastDaySales = []
    totalDay = 0
    lastWeekSales = []
    totalWeek = 0
    lastMonthSales = []
    totalMonth = 0
    vendedores = []
    products = Producto.objects.all()
    salesAll = BasketDb.objects.all()

    last_day = timezone.now() - relativedelta(days=1)
    last_week = timezone.now() - timedelta(days=7)
    last_month = timezone.now() - relativedelta(months=1)

    for sale in salesAll:
        if sale.date_created > last_day:
            lastDaySales.append(sale)
            totalDay += sale.sale_price
        if sale.date_created > last_week:
            lastWeekSales.append(sale)
            totalWeek += sale.sale_price
        if sale.date_created > last_month:
            lastMonthSales.append(sale)
            totalMonth += sale.sale_price

    for vendor in lastDaySales:
        if vendor.vendedor.first_name not in vendedores:
            vendedores.append(vendor.vendedor.first_name)

    context = {'title':"Ventas", 'pagename':pagename, 'salesAll':salesAll, 'vendedores':vendedores, 
                "lastDaySales":lastDaySales, "totalDay":totalDay, 
                "totalWeek":totalWeek, "lastWeekSales":lastWeekSales, 
                "totalMonth":totalMonth, "lastMonthSales":lastMonthSales}
    return render(request, "sales/sales.html", context)


def close_basket(request):
    pagename = "CIERRE DE CAJA"
    lastDaySales = []
    totalDay = 0
    vendedores = []
    perEmploye = []
    sales = 0
    cashPay = 0
    nequiPay = 0
    products = Producto.objects.all()
    salesAll = BasketDb.objects.all()

    last_day = timezone.now() - relativedelta(days=1)
    for sale in salesAll:
        if sale.date_created > last_day:
            lastDaySales.append(sale)
            totalDay += sale.sale_price

    for vendor in lastDaySales:
        if vendor.vendedor.first_name not in vendedores:
            vendedores.append(vendor.vendedor.first_name)

    for vende in vendedores:
        for sale in lastDaySales:
            if sale.vendedor.first_name == vende:
                sales += sale.sale_price

                if sale.pay == "Efectivo":
                    cashPay += sale.sale_price
                if sale.pay == "Nequi":
                    nequiPay += sale.sale_price

        perEmploye.append({vende:{'sales':sales, 'cashPay':cashPay, 'nequiPay':nequiPay}})
        sales = 0
        cashPay = 0
        nequiPay = 0

    context = {'title':"Cierre de Caja", 'pagename':pagename, 'salesAll':salesAll, 'vendedores':vendedores, 
                'perEmploye':perEmploye, 'lastDaySales':lastDaySales, "totalDay":totalDay}
    return render(request, "sales/close_basket.html", context)


def add_product(request, pk):
    basket = Basket(request)
    product = Producto.objects.get(id=pk)
    basket.addition_product(product)
    return redirect("home")


def remove_product(request, pk):
    basket = Basket(request)
    product = Producto.objects.get(id=pk)
    basket.subtract_product(product)
    return redirect("home")


def eliminate_product(request, pk):
    basket = Basket(request)
    product = Producto.objects.get(id=pk)
    basket.delete_product(product)
    return redirect("home")


def clean_basket(request):
    basket = Basket(request)
    basket.wipe_basket()
    return redirect("home")


def save_basket(request, pk):
    from.context_processor import total_basket
    basket = Basket(request)
    total = total_basket(request)
    bask = request.session['basket']
    
    if pk == '1':
        pay = 'Efectivo'
    if pk == '2':
        pay = 'Nequi'

    for ke, val in bask.items():
        product = Producto.objects.get(id=ke)
        for key, value in val.items():
            sale = BasketDb()
            sale.transac_code = "10001"
            sale.vendedor = request.user
            sale.customer = "Mostrador"
            sale.product_id = product.id
            sale.sale_quantity = val['quantity']
            sale.sale_price = val['accumulated']
            sale.pay = pay
        sale.save()
        product.quantity_un -= val['quantity']
        product.save()
        clean_basket(request)
        messages.success(request, f"La venta se guardo satisfactoriamente")
    return redirect("home")

