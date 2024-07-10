from django.shortcuts import render
from bangazonapi.models import *


def ProductsReport(request):

    products_object = Product.objects.filter(price__gt=1000)

    context={
        'products': products_object

    }
    return render(request,'expensiveproducts.html', context)

def StoreReport(request):

    all_stores = Store.objects.all()

    context={
        'stores': all_stores

    }
    return render(request,'allstores.html', context)


def InexpensiveProductsReport(request):
    inexpensive_products_object = Product.objects.filter(price__lte=999)

    context = {
        'products': inexpensive_products_object
    }
    return render(request, 'inexpensiveproducts.html', context)