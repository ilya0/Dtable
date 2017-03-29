from django.conf.urls import url

from . import views

# This is the controller for the app
# and directs to what methods to go to

# when it accesses /polls this is the group to go to
app_name = 'polls'
urlpatterns = [
    # index view
    url(r'^$', views.IndexView.as_view(), name='index'),
    # details view
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # results view
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # vote view
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]



