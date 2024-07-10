from django.shortcuts import render
from bangazonapi.models import *
from django.contrib.auth.models import User

def favoritesellers(request):

    current_user_id = request.GET.get('customer', None)
    current_user_obj = Customer.objects.get(id=current_user_id)
    favorited_objs = Favorite.objects.filter(customer=current_user_obj)

    favorite_sellers = []

    for fav in favorited_objs:
        store = fav.store 
        seller = store.seller
        user = User.objects.get(id=seller.user_id)
        favorite_sellers.append(user)

    context = {
        'current_user_obj': current_user_obj,
        'favorite_sellers': favorite_sellers
    }
    return render(request, 'favoritesellers.html', context)

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


def OrdersReport(request):

    status = request.GET.get('status', None)
    if status == 'incomplete':
        orders = Order.objects.filter(payment_type=None)
    else:
        orders = Order.objects.filter(payment_type__isnull=False)
    context = {
        'orders': orders,
    }
    return render(request, 'incompleteorders.html', context)