from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from about.models import AboutMe


# Create your models here.

class Post(models.Model):
    """
    Model representing a blog post.

    Fields:
    - title (CharField): Title of the post.
    - slug (SlugField): Slug of the post.
    - content (TextField): Content of the post.
    - created_on (DateTimeField): Date and time when the post was created.
    - like (ManyToManyField to User): Users who liked the post.
    - author (ForeignKey to AboutMe): Author of the post.
    - image (ImageField): Image associated with the post.

    Methods:
    - __str__: Returns a string representation of the post.
    - save: Custom save method to generate a slug for the post.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(
        User, default=None, related_name='like_posts', blank=True
    )
    author = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='media/posts/')

    def __str__(self):
        return f"{self.title} | sent by {self.author.artist} "

    def save(self, *args, **kwargs):
        """
        Custom save method to generate a slug for the post.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
