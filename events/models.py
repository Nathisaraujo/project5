from django.db import models

# Create your models here.

class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)    

    def __str__(self):
        return self.title