from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

def products_list(req):
    product = Product.objects.all()
    return render(req, 'products/product_list.html', {'product': product})


@login_required
def product_detail(req, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(req, 'products/product_detail.html', {'product': product})