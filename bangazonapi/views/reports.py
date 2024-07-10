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
