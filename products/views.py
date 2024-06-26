from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductTags
from wishlist.models import Wishlist
from .forms import ProductForm, ProductTagsForm

# Create your views here.


def all_products(request):
    """
    A view to show all the products,
    including sorting and search queries
    """
    products = Product.objects.all()

    query = None
    categories = None
    materials = None
    surfaces = None
    paints = None
    sort = None
    direction = None
    digital = None
    offers = None
    community = None

    if request.GET:
        if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    products = products.annotate(lower_name=Lower('name'))

                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

        if 'material' in request.GET:
            materials = request.GET.getlist('material')
            products = products.filter(
                producttags__materials__name__in=materials
            )

        if 'surface' in request.GET:
            surfaces = request.GET.getlist('surface')
            products = products.filter(producttags__surface__name__in=surfaces)

        if 'paint' in request.GET:
            paints = request.GET.getlist('paint')
            products = products.filter(producttags__paint__name__in=paints)

        if 'digital' in request.GET:
            digital = request.GET['digital']
            products = products.filter(digital=True)

        if 'offers' in request.GET:
            offers = request.GET['offers']
            products = products.filter(offers=True)

        if 'community' in request.GET:
            community = request.GET['community']
            products = products.filter(community=True)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'materials': materials,
        'surfaces': surfaces,
        'paints': paints,
        'digital': digital,
        'offers': offers,
        'community': community,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    wishlist_items = []

    if not isinstance(request.user, AnonymousUser):
        wishlist_items = Wishlist.objects.filter(user=request.user)\
                                 .select_related('product')
    context = {
        'product': product,
        'wishlist_items': [item.product for item in wishlist_items],
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_product_tags(request):
    """ Edit product tags to a specific product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductTagsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product tags!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product tags. Please ensure the form is valid.'
            )
    else:
        form = ProductTagsForm()

    template = 'products/add_product_tags.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product_tags, created = ProductTags.objects.get_or_create(product=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        tags_form = ProductTagsForm(request.POST, instance=product_tags)
        if form.is_valid():
            form.save()
            tags_form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        tags_form = ProductTagsForm(instance=product_tags)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'tags_form': tags_form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
