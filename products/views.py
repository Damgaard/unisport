from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from models import Product

def home(request, category=None, *args, **kwargs):
    """The base page where we display a listing of the cheapest products.

    :param: The product category. Can be kids, kid_adult or women.

    """
    queryset = Product.objects.order_by('price')
    # User has selected a category, narrow down queryset.
    if category:
        qs_kwargs = {category: 1}
        queryset = queryset.filter(**qs_kwargs)

    paginator = Paginator(queryset, 10)
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
    return render(request, "products/listing.html", context)

def details(request, pk, *args, **kwargs):
    """The view for detailed information about a product.

    :param pk: The unique primary key for the product. The name pk is used over
    id as id is the name of a built in function and overriding namespace is a
    bad idea generally.

    """
    product = get_object_or_404(Product, id=pk)
    context = {'product': product}
    return render(request, "products/details.html", context)
