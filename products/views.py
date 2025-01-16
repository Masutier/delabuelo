import csv
import sqlite3 as sql3
import pandas as pd
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from abuemp.decorators import allowed_users, admin_only
from dbs.dbs import db_conn
from .forms import *
from .models import Producto

Sqlite_destiny_path = "dbs/empanadas.db"


@admin_only
def products(request):
    pagename = "PRODUCTOS"
    products = Producto.objects.all()

    context = {'title':"Productos", 'pagename':pagename, 'products':products}
    return render(request, "products/products.html", context)


@admin_only
def createProduct(request):
    pagename = "Crear Producto"
    if request.method == "POST":
        products = Producto.objects.all()
        form = CreateProductForm(request.POST, request.FILES)

        code = request.POST['code']
        name = request.POST['name']

        for product in products:
            if product.code == code and product.name.upper() == name.upper():
                messages.success(request, f"El producto ya existe, utillize la acción [Mod] para modificarlo!")
                return redirect('products')

        if form.is_valid:
            form.save()
            messages.success(request, f"El producto se guardo satisfactoriamente")
            return redirect('products')
    else:
        form = CreateProductForm()

    context = {'title':"Crear Producto", 'pagename':pagename, 'form':form}
    return render(request, "products/create_products.html", context)


@admin_only
def loadCsvProducts(request):
    if request.method == "POST":
        fileinn = request.FILES["loadProducts"]
        nameFile = fileinn.name
        filenamex = nameFile.split('.')

        if filenamex[1] == "xls" or filenamex[1] == "xlsx":
            dataframe = pd.read_excel(fileinn)
        else:
            messages("El archivo no es valido, revise que sea .xls o .xlsx")
            return redirect("/")
        
        dataframe['date_created'] = datetime.now()
        dataframe['date_modify'] = datetime.now()
        messages.success(request,'Se subió correctamente la plantilla de los instructores')
            # DATABASE
        conn = sql3.connect(Sqlite_destiny_path)
        dataframe.to_sql(name="products_producto", con=conn, if_exists="append", index=False)
        conn.close()

        return redirect("products")


@admin_only
def editProduct(request, pk):
    pagename = "Editar Producto"
    product = Producto.objects.get(id=pk)
    form = CreateProductForm(instance=product)

    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'El producto ya quedo modificado!')
            return redirect('products')

    context = {'title':'Editar Producto', 'pagename':pagename, 'form':form}
    return render(request, 'products/edit_product.html', context)


@admin_only
def deleteProduct(request, pk):
    product = Producto.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {'title':'Eliminar Producto', 'item': product}
    return render(request, 'products/delete_product.html', context)

