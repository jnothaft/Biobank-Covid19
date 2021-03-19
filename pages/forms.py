

from django.forms import ModelForm
from django.forms import Textarea
from pages.models import Contact, Request


class ContactForm(ModelForm):
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


class RequestForm(ModelForm):
    class Meta:
        model = Request

        fields = ["first_name", "last_name", "email", "orcid", "institution", "project_title",
                  "project_description", "positive_samples", "negative_samples", "sample_information"
                  ]
