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
    #index page
    url(r'^savedata/', views.IndexView.as_view(), name='savedataindex'),
    #thanks page
    url(r'^thanks/', views.thanks.as_view(), name='thanks'),
    #submitdata to database
    url(r'^submitdata/', views.submitdata, name='submitdata'),
#working routes
    # list of tables - add/delete/modify data
    url(r'^tablelist/', views.tablelist, name='tablelist'),
    #add columns to table
    url(r'^editcolumns/', views.editcolumns, name='editcolumns'),
    #edit-columns_interaction - add data to table
    url(r'^adddata/', views.adddata, name='adddata'),

    url(r'^edittables/', views.edittables, name='edittables'),
    # links to createtable method to submit a new name for a database
    url(r'^createtable/', views.createtable, name='createtable'),
]

