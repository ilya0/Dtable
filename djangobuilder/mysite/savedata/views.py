from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from . import models
# imports all the info from the models file
from .forms import NameForm
from django import forms
import datetime

# this method is not working, currently using the same as index method
######
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'submitform.html', {'form': form})

class thanks(generic.ListView):
    template_name = 'savedata/thanks.html'
    # context_object_name = 'latest_name_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.name.objects.order_by('-pub_date')[:5]


#this is the submit form method
class submitformmethod(generic.ListView):
    template_name = 'savedata/submitform.html'
    context_object_name = 'latest_name_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.name.objects.order_by('-pub_date')[:5]




#this is the index view method
class IndexView(generic.ListView):
    template_name = 'savedata/savedataindex.html'
    context_object_name = 'latest_name_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.name.objects.order_by('-pub_date')[:5]


def redirect(request):
    return HttpResponseRedirect('savedata/submitform')


def submitformroute(request):
    print("submitformroute accessed")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("=== post hit")
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        print("after post request if hit")
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            location = form.cleaned_data["location"]
            # date = form.cleaned_data["pub_date"]
            print(location)
            print(age)
            print(name)
            # print(date)

        # demo of how to create a save objects
        # # creating an user object containing all the data
        # user_obj = User(username=username, email=email, password=password)
        # # saving all the data in the current object into the database
        # user_obj.save()



            myVar = models.name()

            myVar.name = name
            myVar.age = age
            myVar.location = location
            myVar.pub_date = datetime.datetime.now()

            myVar.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        # else:
        #     print(dir(form.errors))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'savedata/submitform.html', {'form': form})


