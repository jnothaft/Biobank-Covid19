import random

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quote, Person
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm
from django.urls import reverse
from django.shortcuts import redirect

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


class PersonPageView(DetailView):
    """Display a single Person object"""
    model = Person  # retrieve Quote objects from the database
    template_name = "quotes/person.html"
    # context_object_name = "person"

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use"""
        # get the default context data:
        # this will include the Person record for this page view
        context  = super(PersonPageView, self). get_context_data(**kwargs)

        # create add image form
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        # return the context dictionary:
        return context



class CreateQuoteView(CreateView):
    """Create a new Quote object and store it in the database"""
    model = Quote
    form_class = CreateQuoteForm
    template_name = "quotes/create_quote_form.html"


class UpdateQuoteView(UpdateView):
    """Create a new Quote object and store it in the database"""
    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote_form.html"
    queryset = Quote.objects.all()


class DeleteQuoteView(DeleteView):
    """Delete a Quote object and store it in the database"""
    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()
    #success_url = "../../all"

    def get_success_url(self):
        """Return  the url to which we should be directed after the delete"""
        # get the pk for this quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first()

        # find the person  associated with the quote
        person = quote.person
        return reverse('person', kwargs={'pk': person.pk})

def add_image(request,pk):
    """A custom view function to handle the submission of an image upload"""

    # find the person for whom we are submitting the image
    person = Person.objects.get(pk=pk)

    # read request data into AddImageForm object
    form = AddImageForm(request.POST or None, request.FILES or None)

    # check if the form is valid, save object to database
    if form.is_valid():
        image = form.save(commit=False)
        image.person = person
        image.save()

    else:
        print("Error: the form was not valid.")

    # redirect to a new url, display person page
    url = reverse('person', kwargs={'pk': pk})
    return redirect(url)
