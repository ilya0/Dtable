from django.conf.urls import url
from . import views

# This is the controller for the app
# and directs to what methods to go to

# when it accesses /polls this is the group to go to
app_name = 'savedata'
urlpatterns = [
    # index view
    url(r'^$', views.IndexView.as_view(), name='savedataindex'),
    url(r'submitform^$', views.get_name, name='get_name'),

]
