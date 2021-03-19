from django.contrib import admin

# Register your models here.
from .models import Contact, Request

admin.site.register(Contact)

admin.site.register(Request)
