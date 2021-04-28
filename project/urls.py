# file: project/urls.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# description: direct URL requests to view functions

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('samples', SamplePageView.as_view(), name='samples'),
    path('contact', ContactCreate.as_view(), name='contact'),
    path('inventory', InventoryView.as_view(), name='inventory'),
    path('thanks', ThankYouView.as_view(), name='thanks'),
    path('order/', OrderCreate.as_view(), name='order'),
    path('orders/<int:pk>', OrderPageView.as_view(), name='orders'),
    path('orders/<int:pk>/update', UpdateOrderView.as_view(), name="update_order"),
    path('orders/<int:pk>/delete', DeleteOrderView.as_view(), name="delete_order"),
    path('services', ServicesView.as_view(), name='services'),
    path('personal/<int:pk>', PersonalPageView.as_view(), name='personal'),
    path('researcher', CreateResearcherView.as_view(), name='researcher'),
    path('sample_upload', sample_upload, name='sample_upload'),
]
