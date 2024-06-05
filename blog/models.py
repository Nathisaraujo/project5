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
    - learn_more_link1 (URLField): First learn more link.
    - learn_more_link2 (URLField): Second learn more link.
    - learn_more_link3 (URLField): Third learn more link.

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
    image = models.ImageField(null=True, blank=True, upload_to='posts/')
    learn_more_link1 = models.URLField(
        blank=True,
        null=True,
        verbose_name="Learn More Link 1"
    )
    learn_more_text1 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Learn More Text 1"
    )
    learn_more_link2 = models.URLField(
        blank=True,
        null=True,
        verbose_name="Learn More Link 2"
    )
    learn_more_text2 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Learn More Text 2"
    )
    learn_more_link3 = models.URLField(
        blank=True,
        null=True,
        verbose_name="Learn More Link 3"
    )
    learn_more_text3 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Learn More Text 3"
    )

    def __str__(self):
        return f"{self.title} | sent by {self.author.artist} "

    def save(self, *args, **kwargs):
        """
        Custom save method to generate a slug for the post.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
