from django.conf.urls import url
from . import views

# This is the controller for the app
# and directs to what methods to go to

# when it accesses /polls this is the group to go to
app_name = 'savedata'
urlpatterns = [

#debug pages
    #shows all the database items
    url(r'show/', views.show),
    #inputboxes to populate the database
    url(r'^submitform/', views.submitform.as_view(), name='submitform'),
    #maybe able to DELETE
    url(r'^savedata/', views.IndexView.as_view(), name='savedataindex'),
    #thanks page
    url(r'^thanks/', views.thanks.as_view(), name='thanks'),
    #testing a def based view
    url(r'^submitformroute/', views.submitformroute, name='submitformroute'),

#working routes
    # list of tables - add/delete/modify data
    url(r'^tablelist/', views.tablelist, name='tablelist'),
    #add columns to table
    url(r'^editcolumns/', views.editcolumns, name='editcolumns'),

    url(r'^edittables/', views.edittables, name='edittables'),
    # links to createtable method to submit a new name for a database
    url(r'^createtable/', views.createtable, name='createtable'),
]

