# mini_fb/views.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# Views for the mini_fb app

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from .models import Profile, StatusMessage
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
    queryset = Profile.objects.all()


# custom classes:
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


class DeleteStatusMessageView(DeleteView):
    """Delete a status message"""
    template_name = "mini_fb/delete_status_form.html"
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use"""
        # obtain default context data
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)

        # find status message
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg'] = st_msg

        return context

    def get_object(self):
        """Return the StatusMessage object that should be deleted"""
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object, and return it
        status = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        return status

    def get_success_url(self):
        """Return  the url to which we should be directed after the delete"""
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        # profile = StatusMessage.objects.get(pk=self.kwargs['profile_pk'])
        # person = profile.profile
        return reverse('show_profile_page', kwargs={'pk': profile_pk})


class ShowNewsFeedView(DetailView):
    """Show the news feed for a profile"""
    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "person"



















