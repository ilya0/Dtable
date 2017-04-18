# this is a new class test
# atributes are variables associated with an instance of class
# a class is a type of thing
# an instance is actual thing

#
# DTable - objects
# DTColumn - objects
# DTColumnType
#     DTColumnTypeText, etc...
# DTSchemaStore
#     DTSchemaStoreJSON
#     DTSchemaStoreSQL
# DTDataEngine
#     DTDataEngineJSON
#     DTDataEngineSQL
from collections import

class DTable:

def __init__(self,id,name,internal_name,columns)
    self.id = id
    self.name =name
    self.internal_name = internal_name
    self.columns = Ordereddict()
    return self

# expect DTcolumn objects
def get_columns(self):
    return self.columns
# add a column to the dynamically generated table
def add_column(table_name, column_name,column_type):
    table = Table(table_name,metadata)
    col = sqlalchemy.Column(column_name, getattr(sa_types, column_type))
    col.create(table,populate_default=True)

def add_column(self,dt_column_object):
    if not (isinstance(dt_column_object,DTColumn)):
            raise Exception("invalid")
        self.columns.append(dt_column_object)


def remove_column(self):

def __repr__(self):
    return "<DTable {}{}{}>".format(self.internal_name, self.id,self.name)



