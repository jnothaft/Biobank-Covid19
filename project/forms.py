# project/forms.py
# Julia Santos Nothaft
# Form page to create forms

from django import forms
from django.forms import ModelForm, SelectMultiple, MultipleChoiceField, CheckboxSelectMultiple, \
    ModelMultipleChoiceField, ChoiceField, Form, RadioSelect, inlineformset_factory
from django.forms import Textarea
from project.models import *


class ContactForm(ModelForm):
    """Form to contact the lab"""

    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "message"]
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Hi! I would like to know more about the process of requesting samples!"
                }
            )
        }


class ResearcherForm(ModelForm, Form):
    """Form to create a new researcher profile"""

    class Meta:
        model = Researcher
        fields = ["first_name", "last_name", "email", "orcid", ]


class ProfileImageForm(ModelForm, Form):
    """Form to upload a image file for the researcher profile pic """
    image = forms.ImageField(required=False)

    class Meta:
        model = ProfileImage
        fields = ["image"]


# options for the checkboxes in the order form
options_info = [('Date of Swab', 'Date of Swab'),
                ('Type of Sample', 'Type of Sample'),
                ('CT values', 'CT values'),
                ('Type of Test', 'Type of Test'),
                ('Result of Test', 'Result of Test')]

# options for the multiple choice in the order form
options_rna = [('Magnetic Bead Extraction', 'Magnetic Bead Extraction'),
               ('Spin Column Extraction', 'Spin Column Extraction'),
               ('No RNA Extraction', 'No RNA Extraction')
               ]


class OrderForm(ModelForm, Form):
    """Form to order COVID-19 samples"""
    # checkbox
    sample_information = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=options_info
    )
    # multiple choice
    RNA_extraction = ChoiceField(
        widget=RadioSelect,
        choices=options_rna
    )

    class Meta:
        # model = Researcher
        # fields = ["first_name", "last_name", "email", "orcid"]

        model = Order
        fields = ["institution", "project_title", "project_description", "positive_samples",
                  "negative_samples", "sample_information", 'RNA_extraction'
                  ]


class UpdateOrderForm(ModelForm, Form):
    """A form to update a Order Form Object"""

    sample_information = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=options_info
    )
    RNA_extraction = ChoiceField(
        widget=RadioSelect,
        choices=options_rna
    )

    class Meta:
        # model = Researcher
        # fields = ["first_name", "last_name", "email", "orcid"]

        model = Order
        fields = ["institution", "project_title", "project_description", "positive_samples",
                  "negative_samples", "sample_information", 'RNA_extraction'
                  ]
