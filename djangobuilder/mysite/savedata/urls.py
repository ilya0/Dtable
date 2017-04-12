from django.conf.urls import url
from . import views

# This is the controller for the app
# and directs to what methods to go to

# when it accesses /polls this is the group to go to
app_name = 'savedata'
urlpatterns = [
    url(r'^savedata/', views.IndexView.as_view(), name='savedataindex'),
    url(r'^submitform/', views.submitform.as_view(), name='submitform'),
    url(r'^thanks/', views.thanks.as_view(), name='thanks'),
    # url(r'^show/', views.show.as_view(), name='name'),
    #testing a def based view of show
   #show route is the route that shows all the values and is workign ****
    url(r'show/', views.show),
    #submit form is the only non-class based view
    url(r'^submitformroute/', views.submitformroute, name='submitformroute'),

    url(r'^tablelist/', views.tablelist, name='tablelist'),
    url(r'^editcolumns/', views.editcolumns, name='editcolumns'),
    #testing new editcolumns
    # url(r'^editcolumns/(?P<table_id>[0-9]+)/$', views.editcolumns, name='editcolumns'),

    url(r'^edittables/', views.edittables, name='edittables'),
    # links to createtable method to submit a new name for a database
    url(r'^createtable/', views.createtable, name='createtable'),
]

