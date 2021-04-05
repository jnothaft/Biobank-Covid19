from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from pages.models import Contact, Order, Samples
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, request
from pages.forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import csv, io
from django.contrib import messages


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
    success_url = "../../thanks"
    template_name = "pages/contact.html"
    # context_object_name = "contact_form"
    contact_form = ContactForm()


class ThankYouView(TemplateView):
    """Create a thank you page after the form is successfully submitted"""
    template_name = "pages/thanks.html"


def thanks(request):
    """Thank you message after the form is submitted"""
    return HttpResponse("Thank you! We will get in touch soon!")


class OrderCreate(LoginRequiredMixin, CreateView):
    """Create fields for the sample request form"""
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("thanks")
    template_name = "pages/order.html"
    success_url = "../../thanks"
    request_form = OrderForm()
    login_url = "/login"


class PersonalPageView(LoginRequiredMixin, TemplateView):
    """user personal page"""
    template_name = "pages/personal.html"
    login_url = "/login"


def sample_upload(request):
    # declaring template
    template_name = "pages/sample_upload.html"
    data = Samples.objects.all()

    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be user_id,test_date,sample_result,test_type,sample_type,collection_site,ct_values',
        'profiles': data
    }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template_name, prompt)
    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Samples.objects.update_or_create(
            user_id=column[0],
            test_dates=column[1],
            sample_results=column[2],
            test_type=column[3],
            sample_type=column[4],
            collection_site=column[5],
            ct_values=column[6]
        )
    context = {}
    return render(request, template_name, context)


class InventoryView(TemplateView):
    """View for the inventory of samples page"""
    template_name = "pages/inventory.html"

    def get_context_data(self, **kwargs):
        # get the data from the default method
        context = super().get_context_data(**kwargs)


def post_status_message(request, pk):
    """
    Process a form submission to post a new status message.
    """

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False)  # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)
