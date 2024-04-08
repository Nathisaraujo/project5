from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Surface, Paint

# Create your views here.

def all_products(request):
    """ A view to show all the products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'material' in request.GET:
            materials = request.GET.getlist('material')
            products = products.filter(producttags__materials__name__in=materials)

        if 'surface' in request.GET:
            surfaces = request.GET.getlist('surface')
            products = products.filter(producttags__surface__name__in=surfaces)
        
        if 'paint' in request.GET:
            paints = request.GET.getlist('paint')
            products = products.filter(producttags__paint__name__in=paints)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }
    
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)