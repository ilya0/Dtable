from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from . import models
from .models import name
from .forms import NameForm
from django import forms
import datetime
import json
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
#sqlachemey print version
print("##sql alchemy version##  "+sqlalchemy.__version__)


# things needed for sqlalchemy
# this is the connection to the database
eng = sqlalchemy.create_engine('postgresql+psycopg2://admin:@localhost:5432/DTabledatabase')
# creates a meta object to hold all the things
meta = MetaData()







def alchemytest():
    cars = Table('Cars', meta,
         Column('Id', Integer, primary_key=True),
         Column('Name', String),
         Column('Price', Integer)
    )
# We create a metadata definition of a Cars table. The table has three columns, defined with the Column class. The datatypes of columns are defined with the Integer and String classes.
    print "The Name column:"
    print cars.columns.Name
    print cars.c.Name

    print "Columns: "
    for col in cars.c:
        print col

    print "Primary keys:"
    for pk in cars.primary_key:
        print pk

    print "The Id column:"
    print cars.c.Id.name
    print cars.c.Id.type
    print cars.c.Id.nullable
    print cars.c.Id.primary_key



#this prints all the tables in in the database
def printdatabases():
    meta.reflect(bind=eng)

    for table in meta.tables:
        print table





# The reflect() method automatically creates Table entries in the MetaData object for any table available in the database but not yet present in the MetaData.

def inspectortest():
    tablename = "savedata_name"
    insp = inspect(eng)
    print insp.get_table_names()
    #get the names of available tables
    print insp.get_columns(tablename)
    #get columns get the names of columns in the tables
    print insp.get_primary_keys(tablename)
    #gets teh primary keys of the
    print insp.get_schema_names()
    #returns all the schema names

inspectortest()




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

        return render(request, 'savedata/show.html', {'form': form})

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



#this is the submit form view
class submitform(generic.ListView):
	template_name = 'savedata/submitform.html'
	context_object_name = 'latest_name_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return models.name.objects.order_by('-pub_date')[:5]


# def submitform(request):
#     print("delete route hit")

#     #renders table page with data from database
#     # going to use this as a test currently
#     thing = name.objects.all() #query the database (this needs to be changed to get the ids and names of all the tables)
#     context = { 'thing': thing }  #this is a dictonary
#     print(context)
#     return render(request, 'savedata/submitform.html', context)

# submitform route method sends the data to the database and then
def submitdata(request):
	print("submitdata accessed")
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


			return HttpResponseRedirect('/adddata/')
		# else:
		#     print(dir(form.errors))
	 # if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()

	return render(request, 'savedata/adddata.html', {'form': form})



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
    # print(context)
    return render(request, 'savedata/table-list.html', context)


def editcolumns(request):
    print("tablelist route hit")
    thing = name.objects.all() #query the database
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/edit-columns.html', context)


def edittables(request):
    print("edit route hit")
    thing = name.objects.all() #query the database
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/table-edit.html', context)




# def createtable(request):
# 	# submits data from input box to create new database
#     print("createtable route hit")
#     #get data from input box
# 	#create new database with name and user id
# 	#pull names
# 	# thing = name.objects.all()
# 	#push results into the context
# 	# context = { 'thing': thing }


#     if request.method == 'POST':
#         post_text = request.POST.get('the_post')
#         response_data = {}

#         name = Name(name=post_text, author=request.user)
#         print("name of name in the createtable route is")
#         print(name)
#         post.save()
#         ##creating a response object that will display
#         response_data['result'] = 'Create post successful!'
#         response_data['postpk'] = name.pk
#         response_data['text'] = name.text
#         response_data['created'] = name.created.strftime('%B %d, %Y %I:%M %p')
#         response_data['author'] = name.author.username

#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )

##testing new way of creating a route

# http://127.0.0.1:8000/createtable/
def createtable(request):
    print("####create table route hit ######")
    post_text = request.POST.get('the_post')
    print("*******text box value is "+post_text)


    return HttpResponse(
        json.dumps({"post_text is": post_text}),
        content_type="application/json"
    )





def rendertablepage(request):
	#renders table page with data from database
	# going to use this as a test currently
    print("rendertablepage route hit")
    thing = name.objects.all() #query the database (this needs to be changed to get the ids and names of all the tables)
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/table-list.html', context)



## currently unused
def deletetable(request):
    print("delete route hit")

	#renders table page with data from database
	# going to use this as a test currently
    thing = name.objects.all() #query the database (this needs to be changed to get the ids and names of all the tables)
    context = { 'thing': thing }  #this is a dictonary
    print(context)
    return render(request, 'savedata/table-list.html', context)


#route which submits data to a table
def adddata(request):
    print("adddata route hit")

    #renders table page with data from database
    # going to use this as a test currently
    #***Need to add a variable to hold the table name
    thing = name.objects.all() #query the database (this needs to be changed to get the ids and names of all the tables)
    # title = name.objects.all() #this needs to be changed to title of the database
    context = { 'thing': thing,
                'title': "Title passed in from selector",
                }  #this is a dictonary
    print(context)
    return render(request, 'savedata/adddata.html', context)









