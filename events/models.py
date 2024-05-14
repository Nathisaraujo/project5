from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, time

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=date.today)
    time = models.TimeField(default=time(0, 0))
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    save_event = models.ManyToManyField(User, related_name='saved_events')

    @property
    def date_and_time(self):
        from datetime import datetime
        return datetime.combine(self.date, self.time)

    def __str__(self):
        return self.title