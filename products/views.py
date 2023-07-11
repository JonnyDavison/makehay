from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products(request):
    """ a view to retuern the products with sort and serch """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
