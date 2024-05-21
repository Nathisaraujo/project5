import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile

# Create your models here.


class Order(models.Model):
    """
    Model representing an order.

    Fields:
    - order_number (CharField): Unique identifier for the order.
    - user_profile (ForeignKey): User profile associated with the order.
    - full_name (CharField): Full name of the customer.
    - email (EmailField): Email address of the customer.
    - phone_number (CharField): Phone number of the customer.
    - country (CountryField): Country of the customer.
    - postcode (CharField): Postal code of the customer.
    - town_or_city (CharField): Town or city of the customer.
    - street_address1 (CharField): First line of the customer's street address.
    - street_address2 (CharField): Scd line of the customer's street address.
    - county (CharField): County, state, or locality of the customer.
    - date (DateTimeField): Date and time when the order was created.
    - delivery_cost (DecimalField): Cost of delivery for the order.
    - order_total (DecimalField): Total cost of the order.
    - grand_total (DecimalField): Grand total cost of the order.
    - original_bag (TextField): Original bag content for the order.
    - stripe_pid (CharField): Stripe payment ID associated with the order.

    Methods:
    - _generate_order_number: Generates a random,
        unique order number using UUID.
    - update_total: Updates the order total and grand total based on line
    item totals and delivery cost.
    - save: Custom save method to set the order number if not already set.
    - __str__: Returns a string representation of the order.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            sdp = settings.STANDARD_DELIVERY_PERCENTAGE
            self.delivery_cost = self.order_total * sdp / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Model representing a line item in an order.

    Fields:
    - order (ForeignKey to Order): Order associated with the line item.
    - product (ForeignKey to Product): Product associated with the line item.
    - quantity (IntegerField): Quantity of the product in the order.
    - lineitem_total (DecimalField): Total cost of the line item.

    Methods:
    - save: Custom save method to set the line item total
    and update the order total.
    - __str__: Returns a string representation of the line item.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
