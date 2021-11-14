'''define url format in learning_logs'''

from django.urls import path
from . import views

urlpatterns = [
    #homepaged
    path(r'', views.index, name='index'),
]