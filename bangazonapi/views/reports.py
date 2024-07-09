from django.shortcuts import render
from bangazonapi.models import *

def favoritesellers(request, pk):

    current_user = Customer.objects.get(id=pk)
    favorite_sellers = Favorite.objects.filter(customer=current_user)

    context = {
        'current_user': current_user,
        'favorite_sellers': favorite_sellers
    }
    return render(request, 'favoritesellers.html', context)
