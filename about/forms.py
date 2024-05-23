from django import forms
from .models import AboutMe
from django_summernote.widgets import SummernoteWidget

class AboutMeForm(forms.ModelForm):
    """
    Form for updating the About Me page.
    Admin can update artist name, title, content, and image.
    """
    class Meta:
        model = AboutMe
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
        }
