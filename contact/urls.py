# contact/urls.py

from django.urls import path
from .views import ContactCreate, thanks

urlpatterns = [
    path("", ContactCreate.as_view(), name="contact"),
    path("thanks/", thanks, name="thanks")

]
