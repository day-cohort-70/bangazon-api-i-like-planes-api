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


def CompletedOrders(request):

    completed_orders = Order.objects.filter(payment_type_id__isnull=False)

    completed_orders_for_html = []

    for order in completed_orders:

        user = User.objects.get(id=order.customer.user_id)

        completed_order_temp = {}
        completed_order_temp["order_id"] = order.id
        completed_order_temp["customer_name"] = user.first_name
        completed_order_temp["total_paid"] = order.total_price
        completed_order_temp["payment_type"] = order.payment_type
        completed_orders_for_html.append(completed_order_temp)


    context={'completed_orders': completed_orders_for_html}

    return render(request,'completedorders.html',context)


def InexpensiveProductsReport(request):
    inexpensive_products_object = Product.objects.filter(price__lte=999)

    context = {
        'products': inexpensive_products_object
    }
    return render(request, 'inexpensiveproducts.html', context)
