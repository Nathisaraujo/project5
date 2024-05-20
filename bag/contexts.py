from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    total_discounted_price = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            if product.offers:
                discounted_price = product.price * (1 - Decimal('0.15'))
                total_discounted_price += discounted_price * item_data
            else:
                discounted_price = product.price
            total += discounted_price * item_data
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'discounted_price': discounted_price,
            })

    delivery = (
        total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        if total < settings.FREE_DELIVERY_THRESHOLD
        else 0
    )
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'total_discounted_price': total_discounted_price,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': (
            max(0, settings.FREE_DELIVERY_THRESHOLD - total)
        ),
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
