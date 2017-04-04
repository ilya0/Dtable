from django.conf.urls import url
from . import views
from django import forms

# This is the controller for the app
# and directs to what methods to go to

# when it accesses /polls this is the group to go to
app_name = 'savedata'
urlpatterns = [
    # index view
    # savedata index goes to save data index
    url(r'^savedata/', views.IndexView.as_view(), name='savedataindex'),
    url(r'^submitform/', views.submitformmethod.as_view(), name='submitform'),
    #creating submit route, dont know if it is going to work yet
    url(r'^submitformroute/', views.submitformroute, name='submitformroute'),

]

