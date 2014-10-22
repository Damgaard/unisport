from django.http import HttpResponse
from django.shortcuts import render

from models import Product

def home(request, *args, **kwargs):
    """The base page where we display a listing of the cheapest products."""
    listing = Product.objects.order_by('price')[:10]
    context = {'listing': listing}
    return render(request, "products/base.html", context)
