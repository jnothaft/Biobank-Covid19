# forms.py

from django import forms
from .models import Quote


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
