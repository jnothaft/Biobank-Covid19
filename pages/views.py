from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from pages.models import Contact, Order
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from pages.forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


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
    """Create fields for the Contact Us page"""
    model = Contact
    # fields = ContactForm
    form_class = ContactForm
    success_url = reverse_lazy("thanks")
    template_name = "pages/contact.html"
    # context_object_name = "contact_form"
    contact_form = ContactForm()


def thanks(request):
    """Thank you message after the form is submitted"""
    return HttpResponse("Thank you! We will get in touch soon!")


class OrderCreate(LoginRequiredMixin, CreateView):
    """Create fields for the sample request form"""
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("thanks")
    template_name = "pages/order.html"
    success_url = reverse_lazy("OrderAuth")
    request_form = OrderForm()
    login_url = "/login"


class PersonalPageView(LoginRequiredMixin, TemplateView):
    """user personal page"""
    template_name = "pages/personal.html"
    login_url = "/login"
