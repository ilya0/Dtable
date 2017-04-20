import collections
# import dtschemastoreapp
from sqlalchemy import *
import models


print("dtableapp imported")

class DTColumn:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type





class DTable:
    # The class "constructor" - It's actually an initializer
    def __init__(self, name):
        #id and name and other params will be added when item is added to database
        self.name = name
        # this will be the columns array
        self.columns = [] #array of all the column OBJECTS
        self.column_names = {} #hash will be the actual data of that object


    # get the columns of the current table
    def get_columns(self):
        return self.columns
    #this will print out the array




    #adds columns to the table requested
    def add_column(self, input):
        # typecheck if input is is an instance
        if not(isinstance(input, DTColumn)):
            raise Exception("not a class of DTColumn")
        #this going to add the thing to the list

        #need to check for duplicate names - add another data structure

        name = input.name
        if name in self.column_names:
            raise Exception("duplicate column name")
        # store name of the column to compare later
        self.column_names[name] = 1
        # store the data
        self.columns.append(input)





    def remove_column(self, name):
        newcolumns = []

        for x in self.columns:
            if name == x.name:
                del self.column_names[name]
            else:
                newcolumns.append(x)

        self.columns = newcolumns







