import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from checkout.models import Order
from products.models import PersonalisedProduct

# Create your models here.

class OrderPersonalised(models.Model):
    SIZE_CHOICES = [
        ('A4', 'A4'),
        ('A5', 'A5'),
        ('A6', 'A6'),
    ]

    PAPER_CHOICES = [
        ('Textured', 'Textured'),
        ('Smooth', 'Smooth'),
        ('Tan', 'Tan'),
        ('Black', 'Black'),
    ]

    FRAME_CHOICES = [
        ('No frame', 'No frame'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Brown', 'Brown'),
    ]

    SUBJECT_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]

    SIZE_PRICES = {
        'A4': 5.00,
        'A5': 4.00,
        'A6': 3.00,
    }

    PAPER_PRICES = {
        'Textured': 3.00,
        'Smooth': 1.00,
        'Tan': 2.00,
        'Black': 2.00,
    }

    FRAME_PRICES = {
        'No frame': 0.00,
        'White': 1.00,
        'Black': 1.00,
        'Brown': 1.00,
    }

    SUBJECT_PRICES = {
        '1': 1.00,
        '2': 2.00,
        '3': 3.00,
        '4': 4.00,
        '5': 5.00,
        '6': 6.00,
        '7': 7.00,
        '8': 8.00,
        '9': 9.00,
        '10': 10.00,
    }

    order_number = models.CharField(max_length=32, null=False, editable=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
    name = models.CharField(max_length=254)
    message = models.TextField()
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='A4')
    paper = models.CharField(max_length=10, choices=PAPER_CHOICES, default='Textured')
    frame = models.CharField(max_length=10, choices=FRAME_CHOICES, default='No frame')
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES, default='Subject 1')


    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def calculate_total_price(self):
        """
        Calculate the total price based on the selected options.
        """
        total_price = 10.00
        total_price += self.SIZE_PRICES.get(self.size, 0)
        total_price += self.PAPER_PRICES.get(self.paper, 0)
        total_price += self.FRAME_PRICES.get(self.frame, 0)
        total_price += self.SUBJECT_PRICES.get(self.subject, 0)
        return total_price


    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.price = self.calculate_total_price()
        self.order_total = self.price

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

class PersonalisedOrderLineItem(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    personalised_product = models.ForeignKey(PersonalisedProduct, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'Personalised Order - {self.order.order_number}'