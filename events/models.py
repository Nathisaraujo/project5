from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, time

# Create your models here.


class Event(models.Model):
    """
    Model representing an event.

    Fields:
    - title (CharField): Title of the event.
    - description (TextField): Description of the event.
    - date (DateField): Date of the event, defaults to today's date.
    - time (TimeField): Time of the event, defaults to midnight.
    - location (CharField): Location of the event.
    - organizer (CharField): Organizer of the event.
    - save_event (ManyToManyField to User): Users who have saved the event.

    Property Methods:
    - date_and_time: Returns the combined date and time of the event.

    Methods:
    - __str__: Returns the title of the event as its string representation.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=date.today)
    time = models.TimeField(default=time(0, 0))
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    save_event = models.ManyToManyField(User, related_name='saved_events')

    @property
    def date_and_time(self):
        """
        Returns the combined date and time of the event.
        """
        from datetime import datetime
        return datetime.combine(self.date, self.time)

    def __str__(self):
        """
        Returns the title of the event as its string representation.
        """
        return self.title