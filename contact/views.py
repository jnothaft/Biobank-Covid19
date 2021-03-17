# contact/views.py
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .cform import ContactForm


# Create your views here.
class ContactCreate(CreateView):
    """Create contact fields"""
    model = Contact
    # fields = ContactForm
    form_class = ContactForm
    success_url = reverse_lazy("thanks")


def thanks(request):
    """Thank you message after the form is submitted"""
    return HttpResponse("Thank you! We will get in touch soon!")
