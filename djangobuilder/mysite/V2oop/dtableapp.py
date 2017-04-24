import collections #this can be used for dict
# import dtschemastoreapp
# import models
# import dtschemastoreapp

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




    #adds columns to the table requested - takes object
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

        #if the item exists
        for x in self.columns:
            if name == x.name:
                del self.column_names[name]
            else:
                newcolumns.append(x)

        self.columns = newcolumns

# not working at the momement
    # def print_columns(self):
    #     counter = 0
    #     for x in self.columns:
    #         print(x.[counter])
    #         counter+=2





# works with the actual data and modifies the actual data table
class dtabledata:

    def __init__(self, schema, data_engine)
        self.schema = schema
        self.data_engine = data_engine
        pass
    pass

    def get_row_by_id(self,id):
        row = self.data_engine.get_row(self.schema,id)
        return row
    pass

    def list_row(self,id):
    pass






#returns a viewable print representation of the object
    def __str__(self):

        return "<DTable  {} {} {}>".format(self.name, self.columns, self.column_names)
            # prints a printable representation  of the object



