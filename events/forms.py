from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    Form for creating and updating events.

    Fields:
    - title (CharField): Title of the event.
    - description (TextField): Description of the event.
    - date (DateField): Date of the event, rendered as a date input.
    - time (TimeField): Time of the event, rendered as a time input.
    - location (CharField): Location of the event.
    - organizer (ForeignKey to User): Organizer of the event.
    """
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'date',
            'time',
            'location',
            'organizer'
        ]
