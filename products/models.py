from django.db import models


class Category(models.Model):
    """
    Model representing a product category.

    Fields:
    - name (CharField): Name of the category.
    - friendly_name (CharField, optional): Friendly name of the category.

    Methods:
    - __str__: Returns a string representation of the category.
    - get_friendly_name: Returns the friendly name of the category.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model representing a product.

    Fields:
    - category (ForeignKey to Category, nullable): Category of the product.
    - sku (CharField, nullable): Stock keeping unit of the product.
    - name (CharField): Name of the product.
    - description (TextField): Description of the product.
    - price (DecimalField): Price of the product.
    - image_url (URLField, optional): URL of the product image.
    - image (ImageField, optional): Image of the product.
    - digital (BooleanField): Indicates if the product is digital.
    - offers (BooleanField): Indicates if the product has offers.
    - community (BooleanField): Indicates if the product is community-related.

    Methods:
    - __str__: Returns a string representation of the product.
    """
    DIGITAL_CHOICES = [
        (True, '0'),
        (False, '1'),
    ]

    OFFERS_CHOICES = [
        (True, '0'),
        (False, '1'),
    ]

    COMMUNITY_CHOICES = [
        (True, '0'),
        (False, '1'),
    ]

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    digital = models.BooleanField(default=False)
    offers = models.BooleanField(default=False)
    community = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductTags(models.Model):
    """
    Model representing product tags.

    Fields:
    - product (OneToOneField to Product): Product associated with the tags.
    - materials (ManyToManyField to Material):
        Materials related to the product.
    - surface (ManyToManyField to Surface): Surfaces related to the product.
    - paint (ManyToManyField to Paint): Paints related to the product.
    - frame (ManyToManyField to Frame): Frames related to the product.
    - paper (ManyToManyField to Paper): Papers related to the product.

    Methods:
    - __str__: Returns a string representation of the associated product.
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    materials = models.ManyToManyField('Material')
    surface = models.ManyToManyField('Surface')
    paint = models.ManyToManyField('Paint')
    frame = models.ManyToManyField('Frame')
    paper = models.ManyToManyField('Paper')

    def __str__(self):
        return str(self.product)

# The following models are related to the ProductTags model above

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Paint(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Surface(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Paper(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Frame(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
