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
    """For to order COVID-19 samples"""

    class Meta:
        model = Researcher
        fields = ["first_name", "last_name", "email", "orcid"]


options_info = [('Date of Swab', 'Date of Swab'),
           ('Type of Sample', 'Type of Sample'),
           ('CT values', 'CT values'),
           ('Type of Test', 'Type of Test'),
           ('Result of Test', 'Result of Test')]

options_rna = [('Magnetic Bead Extraction','Magnetic Bead Extraction'),
               ('Spin Column Extraction', 'Spin Column Extraction'),
               ('No RNA Extraction', 'No RNA Extraction')
]


class OrderForm(ModelForm, Form):
    """For to order COVID-19 samples"""

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
