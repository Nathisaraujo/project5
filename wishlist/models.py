from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Wishlist(models.Model):
    """
    Model to represent a user's wishlist.

    Fields:
    - user (ForeignKey): The user associated with the wishlist.
    - product (ForeignKey): The product added to the wishlist.

    Methods:
    - __str__: Returns a string representation of the wishlist item.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
