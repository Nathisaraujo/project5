from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from .models import (
    Product,
    Category,
    ProductTags,
    Material,
    Surface,
    Paint,
    Frame,
    Paper
)


class ProductForm(forms.ModelForm):
    """
    Form for adding or editing a product.

    This form includes a custom clearable file input widget for the image field.
    """
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductTagsForm(forms.ModelForm):
    """
    Form for adding or editing product tags.

    This form customizes queryset for related fields and sets CSS classes.
    """
    class Meta:
        model = ProductTags
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['materials'].queryset = Material.objects.all()

        self.fields['surface'].queryset = Surface.objects.all()

        self.fields['paint'].queryset = Paint.objects.all()

        self.fields['frame'].queryset = Frame.objects.all()

        self.fields['paper'].queryset = Paper.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark'
