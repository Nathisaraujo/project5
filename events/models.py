from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    save_event = models.ManyToManyField(User, related_name='saved_events')

    def __str__(self):
        return self.title