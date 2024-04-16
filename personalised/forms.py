from django import forms
from .models import OrderPersonalised


class PersonalisedOrderForm(forms.ModelForm):
    class Meta:
        model = OrderPersonalised
        fields = ('name', 'message', 'image',
                  'size', 'paper',
                  'frame', 'subject',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'message': 'Description of the design',
            'image': 'Upload a reference photo here',
        }


