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
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )