Current goals
-------------
Create a DTable constructor that creates DTable objects that have 
id, name, internal, columns via ordered dict, also 


connecting database
https://www.blog.pythonlibrary.org/2010/09/10/sqlalchemy-connecting-to-pre-existing-databases/

  Dtable - creates the objects that will represent the tables that the users will implement
  DTSchemastore - schema from database, compare the database object with the dtable object and also get objects from tdtable
  Dtengine - deals with user defined data and applying it to the database
  
Example of the DTable object

DTable(name: "test", [DTColumn(name:"a", type:integer)], {"a","array","of","column","names"))












# this is a new class test
# atributes are variables associated with an instance of class
# a class is a type of thing
# an instance is actual thing

#
# DTable - objects
# DTColumn - objects
# DTColumnType
#     DTColumnTypeText, etc...

# DTSchemaStore - stores the schema, only responsable for tables in existance
#     DTSchemaStoreJSON
#     DTSchemaStoreSQL

# DTDataEngine - stores the data
#     DTDataEngineJSON
#     DTDataEngineSQL

object and files

# sqlstore = DTSchemaStoreSQL(db) - database connection
# datastore = DTDataEngineSQL(db) - database connection

# schema = sqlstore.get_schema(12342)
# schema.add_column(DTColumn('name', 'text'))

# sqlstore.set_schema(12342, schema)
# datastore.set_schema(12342, schema)



from collections import

class DTable:

        def __init__(self, id, name, internal_name, columns)
        self.id = id
        self.name = name
        self.internal_name = internal_name
        self.columns = Ordereddict()
        return self

    # expect DTcolumn objects
    def get_columns(self):
        return self.columns

    # add a column to the dynamically generated table
    def add_column(table_name, column_name, column_type):
        table = Table(table_name, metadata)
        col = sqlalchemy.Column(column_name, getattr(sa_types, column_type))
        col.create(table, populate_default=True)

    def add_column(self, dt_column_object):
        if not (isinstance(dt_column_object, DTColumn)):
            raise Exception("invalid")
        self.columns.append(dt_column_object)

    def remove_column(self):

    def __repr__(self):
        return "<DTable {}{}{}>".format(self.internal_name, self.id, self.name)
    #show text as string





class DTSchemeStore

    def compairquery

    def setschemea
        #get a hash
        #compair the hashes and delete teh id
        #when you have an id left then you delete it
    return "Dtschemastore"



class DTDataEngine
        return "DTDataengine"
