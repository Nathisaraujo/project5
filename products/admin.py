from django.contrib import admin
from .models import Product, Category, ProductTags, Material, Frame, Paper, Paint, Surface

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class SurfaceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class PaintAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class FrameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class PaperAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Material, MaterialAdmin)
admin.site.register(Surface, SurfaceAdmin)
admin.site.register(Paint, PaintAdmin)
admin.site.register(Frame, FrameAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductTags)

