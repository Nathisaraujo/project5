from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    DIGITAL_CHOICES = [
        (True, '0'),
        (False, '1'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ProductTags(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    materials = models.ManyToManyField('Material')    
    surface = models.ManyToManyField('Surface')    
    paint = models.ManyToManyField('Paint')    
    frame = models.ManyToManyField('Frame')  
    paper = models.ManyToManyField('Paper')
    

    def __str__(self):
        return str(self.product)

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

    

