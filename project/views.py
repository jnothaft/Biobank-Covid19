# project/admin.py
# Julia Santos Nothaft
# Views of the web application

from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.base import View

from project.models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, request, HttpResponseRedirect
from project.forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import csv, io
from django.contrib import messages
from django.forms.models import inlineformset_factory


# Create your views here.


class BasePageView(TemplateView):
    """ A specialized version of List View to display all samples information"""

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use"""
        # obtain default context data
        context = super(BasePageView, self).get_context_data(**kwargs)

        # find status message
        researchers = Researcher.objects.all()
        context['researchers'] = researchers
        return context


class HomePageView(BasePageView):
    """ A specialized version of Template View to display our home page"""
    model = Researcher
    template_name = "project/home.html"
    context_object_name = 'researchers'


class AboutPageView(BasePageView):
    """ A specialized version of Template View to display our about page"""

    template_name = "project/about.html"


class SamplePageView(BasePageView, ListView):
    """ A specialized version of List View to display all samples information"""
    model = Samples
    template_name = "project/samples.html"
    context_object_name = 'samples'

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use"""
        self.object_list = self.get_queryset()
        # obtain default context data
        context = super(SamplePageView, self).get_context_data(**kwargs)

        # find status message
        samples = Samples.objects.all()
        context['samples'] = samples
        return context


class ContactCreate(CreateView, BasePageView):
    """Create fields for the Contact Us page"""
    model = Contact
    # fields = ContactForm
    form_class = ContactForm
    success_url = "../../thanks"
    template_name = "project/contact.html"
    # context_object_name = "contact_form"
    contact_form = ContactForm()
    object = None

    # def get_object(self, queryset=None):
    #     """Return the Order object that should be deleted"""
    #     self.object = self.get_object()
    #     # read the URL data values into variables
    #     contact_pk = self.kwargs['pk']
    #
    #     # find the Order object, and return it
    #     contact = Contact.objects.get(pk=contact_pk)
    #     return contact
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()  # assign the object to the view
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class ThankYouView(BasePageView):
    """Create a thank you page after the form is successfully submitted"""
    template_name = "project/thanks.html"


class OrderCreate(LoginRequiredMixin, CreateView, BasePageView):
    """Create fields for the sample request form"""
    model = Order
    form_class = OrderForm
    template_name = "project/order_form.html"
    # success_url = reverse_lazy("thanks")
    success_url = "../../thanks"
    request_form = OrderForm()
    login_url = "/login"
    object = None

    def form_valid(self, form):
        """attach the researcher to the logged in user"""
        # save the form to obtain an object
        self.object = form.save(commit=False)
        # attach the logged in user to the 'username' attribute of this model's data
        self.object.researcher = Researcher.objects.filter(user=self.request.user).first()
        self.object.save()  # save to the database
        return HttpResponseRedirect(self.get_success_url())


# fix this one
class OrderPageView(LoginRequiredMixin, DetailView):
    """Display a single order object"""
    model = Order  # retrieve Quote objects from the database
    template_name = "project/view_order.html"
    context_object_name = "orders"
    login_url = "/login"

    # def get_context_data(self, **kwargs):
    #     """Return a dictionary with context data for this template to use"""
    #     self.object_list = self.get_queryset()
    #     # obtain default context data
    #     context = super(OrderPageView, self).get_context_data(**kwargs)
    #
    #     # find status message
    #     order = Order.objects.all()
    #     context['order'] = order
    #     return context
    #
    # def get_object(self):
    #     """Return the Order object that should be deleted"""
    #     # read the URL data values into variables
    #     order_pk = self.kwargs['pk']
    #     self.object = self.object_list()
    #
    #     # find the Order object, and return it
    #     order = Order.objects.get(pk=self.kwargs['pk'])
    #     return order

    # # def get_success_url(self):
    # #     """Return  the url to which we should be directed after the delete"""
    # #     # get the pk for this order
    # #     pk = self.kwargs.get('pk')
    # #
    # #     # get the order associated with the pk
    # #     order = Order.objects.filter(pk=pk).first()
    #
    #     # find the researcher associated with the order
    #     researcher = order.researcher
    #
    #     # reverse to the personal/pk url associated with the researcher logged in
    #     return reverse('view_order', kwargs={'pk': researcher.pk})


# fix this one
class UpdateOrderView(LoginRequiredMixin, UpdateView):
    """View to update the order form"""
    model = Order
    form_class = UpdateOrderForm
    template_name = "project/update_order.html"
    login_url = "/login"
    queryset = Order.objects.all()


# fix this one
class DeleteOrderView(LoginRequiredMixin, DeleteView):
    """Delete a order"""
    template_name = "project/delete_order.html"
    queryset = Order.objects.all()
    login_url = "/login"

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use"""

        # obtain default context data
        context = super(DeleteOrderView, self).get_context_data(**kwargs)

        # find status message
        order = Order.objects.get(pk=self.kwargs['pk'])
        context['pk'] = order

        return context

    def get_object(self):
        """Return the Order object that should be deleted"""
        # read the URL data values into variables
        order_pk = self.kwargs['pk']

        # find the Order object, and return it
        order = Order.objects.get(pk=self.kwargs['pk'])
        return order

    def get_success_url(self):
        """Return  the url to which we should be directed after the delete"""
        # reverse to the personal/pk url associated with the researcher logged in
        return reverse('personal', kwargs={'pk': self.get_object().researcher.pk})


class CreateResearcherView(CreateView, LoginRequiredMixin, BasePageView):
    """create a form to add a new researcher"""
    model = Researcher
    form_class = ResearcherForm
    template_name = "project/researcher_form.html"
    # success_url = reverse_lazy("thanks")
    success_url = "../../thanks"
    login_url = "/login"
    object = None

    def form_valid(self, form):
        """attach the researcher to the logged in user"""
        # save the form to obtain an object
        self.object = form.save(commit=False)
        # attach the logged in user to the 'username' attribute of this model's data
        self.object.user = self.request.user
        self.object.save()  # save to the database
        return HttpResponseRedirect(self.get_success_url())


# fix this one
class PersonalPageView(LoginRequiredMixin, DetailView):
    """user personal page"""
    model = Researcher
    template_name = "project/personal.html"
    login_url = "/login"
    context_object_name = "researcher"

    #
    # def get_object(self):
    #     """Return the Order object that should be deleted"""
    #     # read the URL data values into variables
    #     researcher_pk = self.kwargs['pk']
    #
    #     # find the Order object, and return it
    #     order = Order.objects.get(pk=self.kwargs['pk'])
    #     return order

    # def get_context_data(self, **kwargs):
    #     """Return the context data (a dictionary) to be used in the template."""
    #
    #     # obtain the default context data (a dictionary) from the superclass;
    #     # this will include the Profile record to display for this page view
    #     context = super(PersonalPageView, self).get_context_data(**kwargs)
    #     # create a new CreateStatusMessageForm, and add it into the context dictionary
    #     form = OrderForm()
    #     context['order_form'] = form
    #     # return this context dictionary
    #     return context


def sample_upload(request):
    """view to upload a csv file with information about the samples. This function
        was only used to upload data into the samples model, it is not part of the
       overall function of the website.
    """
    # declaring template
    template_name = "project/sample_upload.html"
    data = Samples.objects.all()

    # prompt is a context variable that can have different values depending on their context
    # define prompt with data to be used
    prompt = {
        'profiles': data
    }

    # GET request returns the value of the data with the specified key.
    # if the form is a get method, process the request
    if request.method == "GET":
        return render(request, template_name, prompt)

    # get the file into a variable
    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    # for loop to process csv file into the database
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


class InventoryView(BasePageView):
    """View for the inventory of samples page"""
    template_name = "project/inventory.html"

    # def get_context_data(self, **kwargs):
    #     # get the data from the default method
    #     context = super().get_context_data(**kwargs)


class ServicesView(BasePageView):
    """View for the services information page"""
    template_name = "project/services.html"
