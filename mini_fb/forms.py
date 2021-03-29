# mini_fb/forms.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# Forms for the mini_fb application

from django import forms
from .models import Profile, StatusMessage


class CreateProfileForm(forms.ModelForm):
    """A form to create a new profile"""

    class Meta:
        """Additional data about this form"""

        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email',
                  'image_url']


class UpdateProfileForm(forms.ModelForm):
    """A form to update a new profile"""

    class Meta:
        """Additional data about this form"""

        model = Profile
        fields = ['city', 'email', 'image_url']


class CreateStatusMessageForm(forms.ModelForm):
    """A form to submit a new status message"""
    image = forms.ImageField(required=False)
    class Meta:
        """Additional data about this form"""

        model = StatusMessage
        fields = ['message', 'image']

