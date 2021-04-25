# project/models.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# Database models for the Covid-19 Biobank

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse


class Contact(models.Model):
    """Create a contact form for the Biobank"""
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        """String rep of the name of the person contacting us"""
        return f"{self.first_name} {self.last_name}"


class Researcher(models.Model):
    """Create a profile for a researcher"""
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.EmailField()
    orcid = models.CharField(max_length=16)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        """String rep of the name of the person requesting samples"""
        return f"{self.first_name} {self.last_name}, {self.orcid}"

    def get_order_form(self):
        """get status message for a profile"""
        return Order.objects.filter(researcher=self)

    def get_absolute_url(self):
        """Provide a url to show this object"""
        # profile/<int:pk>
        return reverse('personal', kwargs={'pk': self.pk})


class Order(models.Model):
    """Create a model for the sample request form for the biobank"""
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE, blank=True, null=True)
    institution = models.CharField(max_length=400)
    project_title = models.CharField(max_length=400)
    project_description = models.TextField()
    positive_samples = models.PositiveIntegerField()
    negative_samples = models.PositiveIntegerField()
    sample_information = models.TextField()
    RNA_extraction = models.TextField(blank=True)
    date_request = models.DateField(auto_now_add=True)

    def __str__(self):
        """String rep of the name of the person requesting samples"""
        return f" {self.date_request}: {self.project_title}, {self.researcher} "

    def get_absolute_url(self):
        """Provide a url to show this object"""
        # quote/<int:pk>
        return reverse('orders', kwargs={'pk': self.pk})


class Samples(models.Model):
    """Create a model to store information about the samples in the biobank"""
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.TextField()
    test_dates = models.TextField()
    sample_results = models.TextField()
    test_type = models.TextField()
    sample_type = models.TextField()
    collection_site = models.TextField()
    ct_values = models.TextField(blank=True, null=True)

    def __str__(self):
        """String rep of the name identifying the sample"""
        return f"{self.test_dates}, {self.user_id}: {self.sample_results}"
