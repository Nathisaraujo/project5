from django import forms
from .models import Post
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    """
    Form for creating a blog post.
    """
    class Meta:
        model = Post
        fields = [
            'title', 'content', 'author', 'image',
            'learn_more_link1', 'learn_more_text1',
            'learn_more_link2', 'learn_more_text2',
            'learn_more_link3', 'learn_more_text3'
        ]
        widgets = {
            'content': SummernoteWidget(
                attrs={'summernote': {'width': '100%', 'height': '400px'}}
            ),
            'learn_more_link1': forms.URLInput(
                attrs={'placeholder': 'Add the link here'}
            ),
            'learn_more_text1': forms.TextInput(
                attrs={'placeholder': 'Descriptive text for Link 1'}
            ),
            'learn_more_link2': forms.URLInput(
                attrs={'placeholder': 'Add the link here'}
            ),
            'learn_more_text2': forms.TextInput(
                attrs={'placeholder': 'Descriptive text for Link 2'}
            ),
            'learn_more_link3': forms.URLInput(
                attrs={'placeholder': 'Add the link here'}
            ),
            'learn_more_text3': forms.TextInput(
                attrs={'placeholder': 'Descriptive text for Link 3'}
            ),
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )
