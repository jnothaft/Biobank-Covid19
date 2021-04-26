# project/admin.py
# Julia Santos Nothaft
# Views of the web application


from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from project.models import Contact, Order, Samples
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, request, HttpResponseRedirect
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


class SamplePageView(ListView):
    """ A specialized version of List View to display all samples information"""
    model = Samples
    template_name = "project/samples.html"
    context_object_name = 'samples'


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


class ThankYouDeleteView(TemplateView):
    """Create a thank you page after the form is successfully submitted"""
    template_name = "project/thanks_delete.html"


def thanks(request):
    """Thank you message after the form is submitted"""
    return HttpResponse("Thank you! We will get in touch soon!")

# OrderFormset = inlineformset_factory(
#     Researcher, Order, fields=("institution",
#                                "project_title", "project_description", "positive_samples",
#                                "negative_samples", "sample_information", 'RNA_extraction'),
#     extra=1, can_order=False, can_delete=False
# )


class OrderCreate(LoginRequiredMixin, CreateView):
    """Create fields for the sample request form"""
    model = Order
    form_class = OrderForm
    template_name = "project/order_form.html"
    # success_url = reverse_lazy("thanks")
    success_url = "../../thanks"
    request_form = OrderForm()
    login_url = "/login"

    def form_valid(self, form):
        """attach the researcher to the logged in user"""
        # save the form to obtain an object
        self.object = form.save(commit=False)
        # attach the logged in user to the 'username' attribute of this model's data
        self.object.researcher = Researcher.objects.filter(user=self.request.user).first()
        self.object.save() # save to the database
        return HttpResponseRedirect(self.get_success_url())


class OrderPageView(DetailView):
    """Display a single order object"""
    model = Order  # retrieve Quote objects from the database
    template_name = "project/view_order.html"
    context_object_name = "orders"


class UpdateOrderView(LoginRequiredMixin, UpdateView):
    """View to update the order form"""
    model = Order
    form_class = UpdateOrderForm
    template_name = "project/update_order.html"
    login_url = "/login"
    queryset = Order.objects.all()

    # def get_success_url(self):
    #     """Return  the url to which we should be directed after the update"""
    #     # read the URL data values into variables
    #     researcher_pk = Researcher.kwargs['researcher.pk']
    #
    #     return reverse('personal', kwargs={'pk': researcher_pk})


class CreateResearcherView(CreateView, LoginRequiredMixin):
    """create a form to add a new researcher"""
    model = Researcher
    form_class = ResearcherForm
    template_name = "project/researcher_form.html"
    # success_url = reverse_lazy("thanks")
    success_url = "../../thanks"
    login_url = "/login"

    def form_valid(self, form):
        """attach the researcher to the logged in user"""
        # save the form to obtain an object
        self.object = form.save(commit=False)
        # attach the logged in user to the 'username' attribute of this model's data
        self.object.user = self.request.user
        self.object.save() # save to the database
        return HttpResponseRedirect(self.get_success_url())


class DeleteOrderView(DeleteView):
    """Delete a order"""
    template_name = "project/delete_order.html"
    queryset = Order.objects.all()

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
        # read the URL data values into variables
        # researcher_pk = self.kwargs['profile_pk']
        researcher_pk = self.kwargs['pk']

        # profile = StatusMessage.objects.get(pk=self.kwargs['profile_pk'])
        # person = profile.profile
        # return reverse('personal', kwargs={'pk': researcher_pk})
        return redirect('thanks_delete')

# class OrderCreate(LoginRequiredMixin, CreateView):
#     """Create fields for the sample request form"""
#     model = Researcher
#     form_class = ResearcherForm
#     template_name = "project/order_form.html"
#     success_url = "../../thanks"
#     request_form = ResearcherForm()
#     login_url = "/login"
#
#     def get_context_data(self, **kwargs):
#         # we need to overwrite get_context_data
#         # to make sure that our formset is rendered
#         data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             data["order"] = OrderFormset(self.request.POST)
#         else:
#             data["order"] = OrderFormset()
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         order = context["order"]
#         self.object = form.save()
#         if order.is_valid():
#             order.instance = self.object
#             order.save()
#         return super().form_valid(form)
#

class PersonalPageView(LoginRequiredMixin, DetailView):
    """user personal page"""
    model = Researcher
    template_name = "project/personal.html"
    login_url = "/login"
    context_object_name = "researcher"

    def get_context_data(self, **kwargs):
        """Return the context data (a dictionary) to be used in the template."""

        # obtain the default context data (a dictionary) from the superclass;
        # this will include the Profile record to display for this page view
        context = super(PersonalPageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = OrderForm()
        context['order_form'] = form
        # return this context dictionary
        return context


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
