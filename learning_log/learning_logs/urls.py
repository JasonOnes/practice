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
]
