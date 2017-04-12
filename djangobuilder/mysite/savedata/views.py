from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from . import models
from .models import name
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


# def show(request):
# 	listofthings = name.objects.all()
# 	context = {'listofthings': listofthings}
# 		return render(request, 'savedata/show.html', context)


def redirect(request):
	return HttpResponseRedirect('savedata/submitform')





###########working methods

#this is the index view method
class IndexView(generic.ListView):
	template_name = 'savedata/savedataindex.html'
	context_object_name = 'latest_name_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return models.name.objects.order_by('-pub_date')[:5]



#this is the submit form method
class submitform(generic.ListView):
	template_name = 'savedata/submitform.html'
	context_object_name = 'latest_name_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return models.name.objects.order_by('-pub_date')[:5]



# submitform route method sends the data to the database and then
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
			#creating a my var object to save the parameters
			myVar = models.name()
			#attaching input fields to objects
			myVar.name = name
			myVar.age = age
			myVar.location = location
			myVar.pub_date = datetime.datetime.now()
			myVar.save()

			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:


			return HttpResponseRedirect('/show/')
		# else:
		#     print(dir(form.errors))
	 # if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'savedata/show.html', {'form': form})



class thanks(generic.ListView):
	template_name = 'savedata/thanks.html'
	# context_object_name = 'latest_name_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return models.name.objects.order_by('-pub_date')[:5]



# class show(generic.ListView):
# 	template_name = 'savedata/show.html'
# 	# context_object_name = 'latest_name_list'

# 	def get_queryset(self):
# 		"""Return the last five published questions."""
# 		return models.name.objects.order_by('-pub_date')[:5]




### def based view - this works with the regular routes

def show(request):
    thing = name.objects.all()
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/show.html', context)

def tablelist(request):
    print("tablelist route hit")
    thing = name.objects.all() #query the database
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/table-list.html', context)


def editcolumns(request):
 #needs method for
        return render(request, 'savedata/edit-columns.html', context)


def edittables(request):
    print("edit route hit")
    thing = name.objects.all() #query the database
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/table-edit.html', context)

def createtable(request):
	# submits data from input box to create new database
    print("createtable route hit")

	#get data from input box
	#create new database with name and user id
	#pull names
	# thing = name.objects.all()
	#push results into the context
	# context = { 'thing': thing }

    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        name = Name(name=post_text, author=request.user)
        print("name of name in the createtable route is")
        print(name)
        post.save()
##creating a response object that will display
        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = name.pk
        response_data['text'] = name.text
        response_data['created'] = name.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = name.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def rendertablepage(request):
	#renders table page with data from database
	# going to use this as a test currently
    print("rindertablepage route hit")
    thing = name.objects.all() #query the database (this needs to be changed to get the ids and names of all the tables)
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/table-list.html', context)

def deletetable(request):
    print("delete route hit")

	#renders table page with data from database
	# going to use this as a test currently
    thing = name.objects.all() #query the database (this needs to be changed to get the ids and names of all the tables)
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/table-list.html', context)




#class based view
####### Re-writing the show view

## this works but does not show data

# class show(generic.ListView):
# 	model = name
# 	print("model = name ")
# 	print(model)
# 	#model is a place holder, name is the name of the model already created
# 	context_object_name = 'thing'
# 	#your own name for the list as a template variable'
# 	queryset = name.objects.filter(id__icontains='5') # get names containing a
# 	print("queryset")
# 	print(queryset)
# 	template_name = 'savedata/show.html'


# #this is another way to write it
# class show(generic.ListView):
# 	model = name

# 	def get_queryset(self):
# 		return name.objects.filter(id__icontains='5')[:5]




## testing another way - this works but does not show data
# class show(generic.ListView):
# 	template_name = 'savedata/show.html'
# 	context_object_name = 'thing'

# 	def get_queryset(self):
# 		"""Return the last five published questions."""
# 		print(models.name.objects.order_by('-pub_date')[:5])
# 		return models.name.objects.order_by('-pub_date')[:5]




