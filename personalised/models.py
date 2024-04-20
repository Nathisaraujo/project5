from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Personalised(models.Model):
    SIZE_CHOICES = [
        ('A4', 'A4 - 21.0 x 29.7 cm'),
        ('A5', 'A5 - 14.8 x 21.0 cm'),
        ('A6', 'A6 - 10.5 x 14.8 cm'),
    ]

    ORIENTATION_CHOICES = [
        (True, 'Portrait'),
        (False, 'Landscape'),
    ]

    BRUSHES_CHOICES = [
        ('pen', 'Pen'),
        ('watery_brush', 'Watery Brush'),
        ('chalk', 'Chalk'),
        ('pencil', 'Pencil'),
    ]

    COLOURS_CHOICES = [
        (True, 'Coloured'),
        (False, 'Black & White'),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    name = models.CharField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False) 
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='A4')
    orientation = models.BooleanField(choices=ORIENTATION_CHOICES, default=True)
    brushes = models.CharField(max_length=12, choices=BRUSHES_CHOICES, default='pen')
    colours = models.BooleanField(choices=COLOURS_CHOICES, default=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def __str__(self):
        return self.name
