from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from pages.models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from pages.cform import ContactForm


# Create your views here.

class HomePageView(TemplateView):
    """ A specialized version of Template View to display our home page"""

    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    """ A specialized version of Template View to display our about page"""

    template_name = "pages/about.html"


class SchedulePageView(TemplateView):
    """ A specialized version of Template View to display our schedule page"""

    template_name = "pages/schedule.html"


class ContactCreate(CreateView):
    """Create contact fields"""
    model = Contact
    # fields = ContactForm
    form_class = ContactForm
    success_url = reverse_lazy("thanks")


def thanks(request):
    """Thank you message after the form is submitted"""
    return HttpResponse("Thank you! We will get in touch soon!")
