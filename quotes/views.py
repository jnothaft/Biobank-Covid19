import random

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote


# Create your views here.

class HomePageView(ListView):
    """ Show listing of Quotes"""
    model = Quote  # retrieve Quote objects from the database
    template_name = "quotes/home.html"
    context_object_name = "quotes"


class QuotePageView(DetailView):
    """Display a single quote object"""
    model = Quote  # retrieve Quote objects from the database
    template_name = "quotes/quote.html"
    context_object_name = "quote"


class RandomQuotePageView(DetailView):
    """Display a single quote object"""
    model = Quote  # retrieve Quote objects from the database
    template_name = "quotes/quote.html"
    context_object_name = "quote"

    def get_object(self):
        """Select one quote at random for display in the quote.html templates"""

        # obtain all quotes using the object manager
        quotes = Quote.objects.all()
        # select one at random
        q = random.choice(quotes)
        return q


