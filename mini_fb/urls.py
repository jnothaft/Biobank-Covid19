# mini_fb/urls.py
# Julia Santos Nothaft (jnothaft@bu.edu)
# urls for the mini_fb app
from django.conf.urls.static import static
from django.urls import path

from biobank_database import settings
from .views import *

urlpatterns = [
   path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
   path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
   path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
   path('profile/<int:pk>/post_status', post_status_message, name="post_status"),
   path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name="delete_status"),
   path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name="news_feed"),
   path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name="show_possible_friends"),
   path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name="add_friend"),
   path('create_profile', CreateProfileView.as_view(), name="create_profile"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

# post_status_message.as_view()
