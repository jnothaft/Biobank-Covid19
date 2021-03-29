# mini_fb/urls.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# urls for the mini_fb app
from django.urls import path
from .views import *

urlpatterns = [
   path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
   path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
   path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
   path('profile/<int:pk>/post_status', post_status_message, name="post_status"),
   path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name="delete_status"),
   path('create_profile', CreateProfileView.as_view(), name="create_profile"),
]

# post_status_message.as_view()
