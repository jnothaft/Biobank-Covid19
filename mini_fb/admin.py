# mini_fb/admin.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# Register models
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Profile)
admin.site.register(StatusMessage)
