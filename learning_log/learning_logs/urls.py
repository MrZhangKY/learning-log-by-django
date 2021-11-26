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
]