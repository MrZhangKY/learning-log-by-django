'''define url format in users'''

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    #login page
    path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    
    #logout
    path(r'^logout/$', views.logout_view, name='logout'),
    
    #register page
    path(r'^register/$', views.register, name='register'),
]