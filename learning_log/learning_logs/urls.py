"""Defines the URL patterns for the learning_logs app. Not to be confused
with the urls for learning_log."""

from django.conf.urls import url

from . import views

app_name = "learning_logs"
urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),
    # Topics page, show all topics
    url(r'^topics/$', views.topics, name='topics'),
    # Show a specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Add a new topic page
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # New entry page
    url(r'^new_entry/(?P<topic_id>\d+)$', views.new_entry, name='new_entry'),
    # Edit entry page
    url(r'^edit_entry/(?P<entry_id>\d+)$', views.edit_entry,
        name='edit_entry'),
]
