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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# things needed for sqlalchemy
eng = sqlalchemy.create_engine('postgresql+psycopg2://admin:@localhost:5432/dtabledatabase') # this is the connection to the database
meta = MetaData() # creates a meta object to hold all the things
Base = declarative_base() #declarative base class is created with this function
print("##sql alchemy initialized - version: ##  "+sqlalchemy.__version__) #sqlachemey print version




#this is a method that creates a table when hit from an ajax call
def createtable(request):
    ##*****still needs a method where it will load nontype******
    print("####create table route hit ######")
    tabletitle = request.POST.get('the_post')
    print("*******text box value is "+tabletitle)

    class tableconstructor(Base):
        __tablename__ = tabletitle

        Id = Column(String, primary_key=True)
        col1 = Column(String)
        col2 = Column(String)
        # The user-defined Car class is mapped to the Cars table. The class inherits from the declarative base class.

    Base.metadata.bind = eng
    # The declarative Base is bound to the database engine.
    Base.metadata.create_all()
    # The create_all() method creates all configured tables; in our case, there is only one table.
    Session = sessionmaker(bind=eng)
    ses = Session()
    # A session object is created.
    ses.add_all(
       [tableconstructor(Id=1, col1='Col1Empty1', col2="col2empty1"),
        tableconstructor(Id=2, col1='Col1Empty2', col2="col2empty2")])
        # With the add_all() method, we add the specified instances of Car classes to the session.
    ses.commit()
    # The changes are committed to the database with the commit() method.
    rs = ses.query(tableconstructor).all()
    # We query for all data from the Cars table. The query() method loads all instances of the Car class and its all() method returns all results represented by the query as a list.
    for item in rs:
        print (item.col1, item.col2)
    # We iterate through the result set and print two columns for all returned rows.
    return HttpResponse(
        json.dumps({"tabletitle is": tabletitle}),
        content_type="application/json"
    )





#testing methods


# We create a metadata definition of a Cars table. The table has three columns, defined with the Column class. The datatypes of columns are defined with the Integer and String classes.
def alchemytest():
    cars = Table('Cars', meta,
         Column('Id', Integer, primary_key=True),
         Column('Name', String),
         Column('Price', Integer)
    )
    print("The Name column:")
    print(cars.columns.Name)
    print(cars.c.Name)

    print("Columns: ")
    for col in cars.c:
        print (col)

    print ("Primary keys:")
    for pk in cars.primary_key:
        print (pk)

    print("The Id column:")
    print(cars.c.Id.name)
    print(cars.c.Id.type)
    print(cars.c.Id.nullable)
    print(cars.c.Id.primary_key)



#this prints all the tables in in the database
# The reflect() method automatically creates Table entries in the MetaData object for any table available in the database but not yet present in the MetaData.

def printtables(request):
    print("printtables route hit")
    meta.reflect(bind=eng)

    for table in meta.tables:
        print(table)

    return HttpResponse(
        json.dumps({"tabletitle is": table}),
        content_type="application/json"
    )



#prints out names of ITEMS in a TABLE
# The Inspector performs low-level database schema inspection. An Inspector is created with the inspect() method.

def inspectortest():
    tablename = "savedata_name"
    insp = inspect(eng)
    print(insp.get_table_names())
    #get the names of available tables
    print(insp.get_columns(tablename))
    #get columns get the names of columns in the tables
    print(insp.get_primary_keys(tablename))
    #gets teh primary keys of the
    print(insp.get_schema_names())
    #returns all the schema names

#inspectortest()




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





###def based view - this works with the regular routes

def show(request):
    thing = name.objects.all()
    context = {'thing': thing}  #this is a dictonary
    print(context)
    return render(request, 'savedata/show.html', context)




def edittables(request):
    print("edit route hit")
    thing = name.objects.all() #query the database
    context = {'thing': thing}  #this is a dictonary
    print(context)
    return render(request, 'savedata/table-edit.html', context)





def editcolumns(request):
    print("editcolumns route hit")
    #set default table
    #set table to table selected
    #get contents of table
    #render page

    rendertable = "savedata_name"
    # rendertable = request.POST.get('buttonidholder')

    thing = name.objects.all() #query the database



    context = {'thing': thing}  #this is a dictonary
    print(context)
    return render(request, 'savedata/edit-columns.html', context)





def gettablestructure(request):
    tabletoview = "savedata_name"
    # Create MetaData instance
    metadata = MetaData(eng, reflect=True)
    print(metadata.tables)
    # saves the data from the table in question
    ex_table = metadata.tables[tabletoview]


    for t in metadata.tables[tabletoview]:
        print(t.name)


    return HttpResponse(
        json.dumps({"tabletitle is": "test"}),
        content_type="application/json"
    )






#shows tables in database on page tablelist

def tablelist(request):
    print("tablelist route hit")
    tablelistarray = []
    meta.reflect(bind=eng)

    for table in meta.tables:
        tablelistarray.insert(0,table)
        print(table)
        print('Final array:', tablelistarray)

    context = {'thing': tablelistarray}
    print(context)
    return render(request, 'savedata/table-list.html', context)




#delete table route needs to be changed to get tables by ids
def deletetable(request):
    print("delete route hit")
    tabletodelete = request.POST.get('buttonidholder')
    context = { 'thing': tabletodelete }  #this is a dictonary
    print("table to delete is")
    print(tabletodelete) #sanity checking

    # delete the corresponding table
    table_name = tabletodelete
    table = Table(table_name, meta)
    if table.exists(bind=eng):
        table.drop(bind=eng)
        return render(request, 'savedata/table-list.html', context)

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



#simple redirect route
def redirect(request):
    return HttpResponseRedirect('savedata/submitform')






