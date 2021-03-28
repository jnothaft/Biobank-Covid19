# forms.py

from django import forms
from .models import Quote, Image


class CreateQuoteForm(forms.ModelForm):
    """A form to create a new Quote object"""

    class Meta:
        """Additional data about this form"""
        model = Quote
        fields = ['text', 'person']


class UpdateQuoteForm(forms.ModelForm):
    """A form to update a new Quote object"""

    class Meta:
        """Additional data about this form"""
        model = Quote
        fields = ['text', 'person']


class AddImageForm(forms.ModelForm):
    """A form to collect an image from the user"""

    class Meta:
        model = Image
        fields = ["image_file",]
