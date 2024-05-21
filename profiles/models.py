from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    """
    Model to maintain user profiles.

    Fields:
    - user (OneToOneField): Associated user.
    - default_phone_number (CharField): Default phone number.
    - default_street_address1 (CharField): Default street address line 1.
    - default_street_address2 (CharField): Default street address line 2.
    - default_town_or_city (CharField): Default town or city.
    - default_county (CharField): Default county.
    - default_country (CountryField): Default country.
    - default_postcode (CharField): Default postal code.

    Methods:
    - __str__: Returns the username of the associated user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True
    )
    default_postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function to create or update user profiles.

    Parameters:
    - sender: The model class.
    - instance: The instance being saved.
    - created: True if a new record was created.
    """
    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()


class Recommendation(models.Model):
    """
    Model to store user recommendations.

    Fields:
    - user (ForeignKey): Associated user.
    - recommendation_text (TextField): Text of the recommendation.
    - timestamp (DateTimeField): Timestamp of the recommendation creation.

    Methods:
    - __str__: Returns a string representation of the recommendation.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation by {self.user.username} | ({self.timestamp})"
