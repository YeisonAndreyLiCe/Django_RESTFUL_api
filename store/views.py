from django.shortcuts import render

from store.models import Product, ShoppingCart

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/product_list.html', context)

def show(request, product_id):
    context = {
        'product': Product.objects.get(id=product_id)
    }
    return render(request, 'store/product_show.html', context)

def cart(request):
    context = {
        'items': [],
        'subtotal': 1.0,
        'tax_rate': int(ShoppingCart.TAX_RATE * 100),
        'tax_total': 2.0,
        'total': 3.0
    }
    return render(request, 'store/cart.html', context)