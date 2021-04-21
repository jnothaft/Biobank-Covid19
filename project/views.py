from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from project.models import Contact, Order, Samples
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, request
from project.forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import csv, io
from django.contrib import messages
from django.forms.models import inlineformset_factory


# Create your views here.

class HomePageView(TemplateView):
    """ A specialized version of Template View to display our home page"""

    template_name = "project/home.html"


class AboutPageView(TemplateView):
    """ A specialized version of Template View to display our about page"""

    template_name = "project/about.html"


class SchedulePageView(TemplateView):
    """ A specialized version of Template View to display our schedule page"""

    template_name = "project/schedule.html"


class ContactCreate(CreateView):
    """Create fields for the Contact Us page"""
    model = Contact
    # fields = ContactForm
    form_class = ContactForm
    success_url = "../../thanks"
    template_name = "project/contact.html"
    # context_object_name = "contact_form"
    contact_form = ContactForm()


class ThankYouView(TemplateView):
    """Create a thank you page after the form is successfully submitted"""
    template_name = "project/thanks.html"


def thanks(request):
    """Thank you message after the form is submitted"""
    return HttpResponse("Thank you! We will get in touch soon!")

OrderFormset = inlineformset_factory(
    Researcher, Order, fields=("institution",
                               "project_title", "project_description", "positive_samples",
                               "negative_samples", "sample_information", 'RNA_extraction'),
    extra=1, can_order=False, can_delete=False
)


class OrderCreate(LoginRequiredMixin, CreateView):
    """Create fields for the sample request form"""
    model = Researcher
    form_class = ResearcherForm
    template_name = "project/order.html"
    success_url = "../../thanks"
    request_form = ResearcherForm()
    login_url = "/login"

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["order"] = OrderFormset(self.request.POST)
        else:
            data["order"] = OrderFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        order = context["order"]
        self.object = form.save()
        if order.is_valid():
            order.instance = self.object
            order.save()
        return super().form_valid(form)


class PersonalPageView(LoginRequiredMixin, TemplateView):
    """user personal page"""
    template_name = "project/personal.html"
    login_url = "/login"


def sample_upload(request):
    # declaring template
    template_name = "project/sample_upload.html"
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
    template_name = "project/inventory.html"

    def get_context_data(self, **kwargs):
        # get the data from the default method
        context = super().get_context_data(**kwargs)


class ServicesView(TemplateView):
    """View for the services information page"""
    template_name = "project/services.html"
