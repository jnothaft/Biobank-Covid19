# quotes/models.py
from django.db import models

# Create your models here.


class Quote(models.Model):
    """ Represents a quote by a famous person"""

    # data attributes
    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        """Retrieve a string representation of this quote"""

        return f'"{self.text}" - {self.author}'


