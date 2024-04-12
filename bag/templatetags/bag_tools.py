from django import template
from decimal import Decimal, ROUND_HALF_UP


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name='discount')
def discount(price, percent):
    """
    Calculates the discounted price for a given price and discount percentage.
    """
    price = Decimal(str(price))  # Ensure correct precision for the price
    percent = Decimal(str(percent))  # Ensure correct precision for the percent
    discounted_price = price * (1 - percent / 100)
    return discounted_price.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)