# mini_fb/views.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# Views for the mini_fb app
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile


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
