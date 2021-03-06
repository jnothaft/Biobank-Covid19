# mini_fb/models.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# Models for the mini_fb app
from django.db import models

# Create your models here.
from django.urls import reverse


class Profile(models.Model):
    """Creates a facebook profile for a person"""
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        """Retrieve a string representation of the profile name"""
        return f'{self.first_name} {self.last_name}'

    def get_status_messages(self):
        """get status message for a profile"""
        return StatusMessage.objects.filter(profile=self)

    def get_absolute_url(self):
        """Provide a url to show this object"""
        # profile/<int:pk>
        return reverse('show_profile_page', kwargs={'pk': self.pk})

    def get_friends(self):
        """Return all friends of this profile"""
        queryset = self.friends.all()
        return queryset

    def get_news_feed(self):
        """Obtain and return the news feed messages for a profile"""
        news = StatusMessage.objects.filter(profile__in=self.get_friends()).order_by("-timestamp")
        return news

    def get_friend_suggestions(self):
        """Obtain and return a QuerySet of all Profiles that could be
        added as friends"""
        possible_friends = Profile.objects.exclude(pk__in=self.get_friends())
        possible_friends = possible_friends.exclude(pk=self.pk)

        return possible_friends


class StatusMessage(models.Model):
    """Model the data attributes of Facebook status message"""
    timestamp = models.TimeField(auto_now=True, blank=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        """Retrieve a string representation of the status message"""

        return f'{self.timestamp} {self.profile}'
