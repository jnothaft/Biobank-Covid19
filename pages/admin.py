from django.contrib import admin

# Register your models here.
from .models import Contact, Order

admin.site.register(Contact)

admin.site.register(Order)
