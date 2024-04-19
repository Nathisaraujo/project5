from django import forms
from .models import Personalised


class PersonalisedForm(forms.ModelForm):
    class Meta:
        model = Personalised
        fields = ('name', 'phone_number', 'email',
                  'message', 'size',
                  'orientation', 'brushes', 'colours',)

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


