from django.conf.urls import url
from . import views

# This is the controller for the app
# and directs to what methods to go to

# when it accesses /polls this is the group to go to
app_name = 'savedata'
urlpatterns = [
    # index view
    url(r'^savedataindex/$', views.IndexView.as_view(), name='savedataindex'),
    url(r'savedata/submitform', views.get_name, name='submitform'),

]



# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'fetch$', views.fetch),
