from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for Post model.

    This admin option allows managing Post instances including fields such as
    title, slug, status, created_on, and author. It enables rich text editing
    for the content field using the Summernote editor.
    """

    list_display = ('title', 'slug', 'created_on', 'author')
    search_fields = ['title', 'content']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('title',)}
