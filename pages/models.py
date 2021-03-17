from django.db import models


# Create your models here.

class Contact(models.Model):
    """Create a contact form for the Biobank"""
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    message = models.TextField()

    def __str__(self):
        """String rep of the name of the person contacting us"""
        return f"{self.first_name} {self.last_name}"
