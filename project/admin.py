# project/admin.py
# Julia Santos Nothaft
# Admin page to register models


from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Contact)

admin.site.register(Researcher)

admin.site.register(Order)

admin.site.register(Samples)

