from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
# from . import models
# from .models import name
# from .forms import NameForm
from django import forms
import datetime
import json
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#what dtschemastore does
#creates objects of currently populated databases
#read from database to create object
#gets dtable objects to apply them to the schema and current database




# %%%%database connections
# sqlstore = DTSchemaStoreSQL(db)
# datastore = DTDataEngineSQL(db)
eng = sqlalchemy.create_engine('postgresql+psycopg2://admin:@localhost:5432/dtabledatabase') # this is the connection to the database
meta = MetaData(eng)
# creates a meta object to hold all the things
Base = declarative_base() #declarative base class is created with this function
Session = sessionmaker(bind=eng)





class DTSchemaStoreJSON(object):
    pass








class DTSchemaStoreSQL(object):

    def __init__(self,name):
        self.name = name


        ## gets the columns from the input table by name
    def get_schema(id):
        storedschemacolumns = ""  # storing columns from get_schema
        # tablename = name
        insp = inspect(eng)
        storedschemacolumns = insp.get_columns(id)
        print(storedschemacolumns)
        return (storedschemacolumns)






    def compare_schema(dtableinputobject,currenttablename):
        #this needs to be changed to the comapare schema, but im using the long way for now
        insp = inspect(eng)
        oldschema = insp.get_columns(currenttablename)# query database for current schema

        newschema = dtableinputobject

        oldcolumncount = len(oldschema)
        newcolumncount = len(newschema)

        if oldcolumncount == newcolumncount:
             # for x in columns
            # needs to continue going on the compare
            #if nothing changes then
            # apply data with no schema change
            print("same schema")
        else:
            # change the schema
            # apply the data
            print("different schema")

        # columnholder = []
        # schema = self.session.query(models.Sheets_Schema).filter(models.Sheets_Schema.sheet_id==table_id).all()
        #
        # for col in schema
        #     columnholder.append(DTColumn(col.id,col.column_name,col.column_type))
        #     return dtable(table_id,table_name,dt_columns)





    def add_schema_column(self,dtableobject):
        #dtableobject should have:
        #newtablename
        #newtableID

        pass

    def delete_schema_column(self,id):
        old_column = session.query(Columns).filter_by(id=id).one()
        delete(old_column)
        pass



    def set_schema(dtableobject):
        # set schema takes the dtable object and the creates the connections and sets object into a schema

        # receives and object and applies it to the the database
        # compare the table to the dtable object to see if it is already in existance
        # use the id to compare the table

        # if the id is None - it is a new
        # if there is an id
        metadata = MetaData(eng)
        # Declare a table
        table = Table(dtableobject.name, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))
        # Create
        # all tables
        metadata.create_all()
        for _t in metadata.tables:
            print("Table: ", _t)

       # engine.execute(CreateSchema(newschema))
        pass



        # droping an existing table
    def droptable(dtable):
        sqlalchemy.Table("{}".format(dtable.name),meta).drop()








    def __repr__(self):
        return "<DTable  {} >".format(self.name)
            # prints a printable representation  of the object




