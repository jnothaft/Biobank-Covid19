# mini_fb/views.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# Views for the mini_fb app

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from .models import Profile
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

class ShowAllProfilesView(ListView):
    """ Format the main facebook page"""
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'mini_fb'


class ShowProfilePageView(DetailView):
    """"Display a single profile"""
    model = Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "person"

    def get_context_data(self, **kwargs):
        """Return the context data (a dictionary) to be used in the template."""

        # obtain the default context data (a dictionary) from the superclass;
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context


class CreateProfileView(CreateView):
    """Create a view for the create profile form"""
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"


class UpdateProfileView(UpdateView):
    """Create a view for the create profile form"""
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"


# custom classes:
def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

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
