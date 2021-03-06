'''define url format in learning_logs'''

from django.urls import path
from . import views

urlpatterns = [
    #homepage
    path(r'', views.index, name='index'),
    
    #topic
    path(r'^topics/$', views.topics, name='topics'),
    
    #special topic
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    
    #webpage for adding new topic
    path(r'^new_topic/$', views.new_topic, name='new_topic'),
    
    #webpage for adding new item for topic
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    
    #edit existed item
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]