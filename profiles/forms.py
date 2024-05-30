from django import forms
from .models import UserProfile, Recommendation


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profiles.

    Excludes:
    - user (User): The associated user.
    - default_phone_number (CharField): Default phone number.

    Methods:
    - __init__: Initializes the form with placeholders, classes,
                and removes auto-generated labels.
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'default_phone_number',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input'
            )
            self.fields[field].label = False


class RecommendationForm(forms.ModelForm):
    """
    Form for submitting recommendations.

    Fields:
    - recommendation_text (Textarea): Text field for the recommendation.

    Methods:
    - __init__: Initializes the form with custom label for recommendation_text.
    """
    class Meta:
        model = Recommendation
        fields = ['recommendation_text']
        widgets = {
            'recommendation_text': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recommendation_text'].label = 'Your Recommendation'
