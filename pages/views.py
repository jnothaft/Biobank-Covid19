from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    """ A specialized version of Template View to display our home page"""

    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    """ A specialized version of Template View to display our about page"""

    template_name = "pages/about.html"
