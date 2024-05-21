from django import forms
from .models import Post
from .widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):
    """
    Form for creating a blog post.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )