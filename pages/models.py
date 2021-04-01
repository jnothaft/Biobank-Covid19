from django.db import models


# Create your models here.

class Contact(models.Model):
    """Create a contact form for the Biobank"""
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        """String rep of the name of the person contacting us"""
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    """Create a model for the sample request form for the biobank"""
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.EmailField()
    orcid = models.CharField(max_length=16)
    institution = models.CharField(max_length=400)
    project_title = models.CharField(max_length=400)
    project_description = models.TextField()
    positive_samples = models.PositiveIntegerField()
    negative_samples = models.PositiveIntegerField()
    sample_information = models.TextField()

    def __str__(self):
        """String rep of the name of the person requesting samples"""
        return f"{self.first_name} {self.last_name}, {self.institution}"


class Samples(models.Model):
    """Create a model to store information about the samples in the biobank"""
    user_id = models.TextField()
    test_dates = models.TextField()
    sample_results = models.TextField()
    test_type = models.TextField()
    sample_type = models.TextField()
    collection_site = models.TextField()
    ct_values = models.TextField()

    def __str__(self):
        """String rep of the name identifying the sample"""
        return f"{self.test_dates}, {self.user_id}: {self.sample_results}"
