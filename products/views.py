from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render

from models import Product

def home(request, *args, **kwargs):
    """The base page where we display a listing of the cheapest products."""
    paginator = Paginator(Product.objects.order_by('price'), 10)
    # Add check and handling for no Products
    page = request.GET.get('page')
    try:
        listing = paginator.page(page)
    except PageNotAnInteger:
        # Invalid page requested. Return first page.
        listing = paginator.page(1)
    except EmptyPage:
        # Tried to show an empty page. This will happen if the user manually enters a number
        # exceeding number of pages or if content exists at all. Show the last page, which
        # will cover the first case and handle the second case inside the view.
        listing = paginator.page(paginator.num_pages)
    context = {'listing': listing}
    return render(request, "products/base.html", context)
