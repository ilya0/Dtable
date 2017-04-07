from django.conf.urls import url
from . import views
from django import forms

# This is the controller for the app
# and directs to what methods to go to

# when it accesses /polls this is the group to go to
app_name = 'savedata'
urlpatterns = [


    url(r'^savedata/', views.IndexView.as_view(), name='savedataindex'),
    url(r'^submitform/', views.submitform.as_view(), name='submitform'),
    url(r'^thanks/', views.thanks.as_view(), name='thanks'),
    url(r'^show/', views.show.as_view(), name='show'),

    #submit form is the only non-class based view
    url(r'^submitformroute/', views.submitformroute, name='submitformroute'),


]

