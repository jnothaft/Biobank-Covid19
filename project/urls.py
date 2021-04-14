# file: project/urls.py
# description: direct URL requests to view functions

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('schedule', SchedulePageView.as_view(), name='schedule'),
    path('contact', ContactCreate.as_view(), name='contact'),
    path('inventory', InventoryView.as_view(), name='inventory'),
    path('thanks', ThankYouView.as_view(), name='thanks'),
    path('order', OrderCreate.as_view(), name='order'),
    path('services', ServicesView.as_view(), name='services'),
    path('personal', PersonalPageView.as_view(), name='personal'),
    path('sample_upload', sample_upload, name='sample_upload'),
]