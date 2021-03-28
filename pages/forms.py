from django.forms import ModelForm, SelectMultiple, MultipleChoiceField, CheckboxSelectMultiple, \
    ModelMultipleChoiceField, ChoiceField, Form
from django.forms import Textarea
from pages.models import Contact, Order


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


options = [('Date of Swab', 'Date of Swab'),
           ('Type of Sample', 'Type of Sample'),
           ('Collection Site', 'Collection Site'),
           ('Type of Test', 'Type of Test')]


class OrderForm(ModelForm, Form):
    """For to order COVID-19 samples"""
    sample_information = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=options
    )

    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "orcid", "institution", "project_title",
                  "project_description", "positive_samples", "negative_samples", "sample_information"
                  ]

