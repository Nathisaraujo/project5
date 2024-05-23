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
        fields = ['title', 'content', 'author', 'image']
        widgets = {
            'description': SummernoteWidget(),
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )