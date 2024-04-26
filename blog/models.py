from django.db import models
from django.contrib.auth.models import User
from about.models import AboutMe

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(
        User, default=None, related_name='like_posts', blank=True
    )
    author = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='media/posts')

    def __str__(self):
        return f"{self.title} | sent by {self.author.artist} "