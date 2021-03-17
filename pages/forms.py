

from django.forms import ModelForm
from django.forms import Textarea
from pages.models import Contact


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
