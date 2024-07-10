from django.shortcuts import render
from bangazonapi.models import *

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