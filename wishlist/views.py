from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from wishlist.models import Wishlist

# Relied on a colleague views to create the wishlist views - refer to README


@login_required
def add_to_wishlist(request, product_id):
    """
    This view adds a product to the user's wishlist
    and redirects the user to the product detail page.
    If the product is already in the user's wishlist,
    it displays an error message
    """
    product = get_object_or_404(Product, pk=product_id)
    exist_wishlist_item = Wishlist.objects.filter(product=product, user=request.user)

    if not exist_wishlist_item:
        Wishlist.objects.create(product=product, user=request.user)
        messages.success(request, 'Product added to wishlist!')
    else:
        messages.error(request, 'Product already in wishlist!')

    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    """
    This view removes a product from the user's wishlist
    and redirects the user to the product detail page.
    """
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    messages.success(request, 'Item removed from your wishlist!')
    return redirect('product_detail', product_id=product_id)
