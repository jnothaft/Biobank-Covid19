# mini_fb/models.py
from django.db import models


# Create your models here.

class Profile(models.Model):
    """Creates a facebook profile for a person"""
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        """Retrieve a string representation of the profile name"""

        return f'{self.first_name} {self.last_name}'
