from django.db import models


class AboutMe(models.Model):
    """
    Model representing the About Me page.
    Includes fields for artist name, title, content, image URL, and image.
    """
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=254)
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.artist
