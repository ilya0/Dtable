
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#what dtschemastore does
#creates objects of currently populated databases
#read from database to create object
#gets dtable objects to apply them to the schema and current database




#%%%%database connections
# sqlstore = DTSchemaStoreSQL(db)
# datastore = DTDataEngineSQL(db)
eng = sqlalchemy.create_engine('postgresql+psycopg2://admin:@localhost:5432/dtabledatabase') # this is the connection to the database
meta = MetaData()
# creates a meta object to hold all the things
Base = declarative_base() #declarative base class is created with this function
Session = sessionmaker(bind=eng)






class dtschemastoreSQL(object):

    def __init__(self,name):
        self.name = name


    #takes two objects and compares them so that the change can be implemented in to the schema
    #returns the changes that should be made?


    # def compare_schema(self,input):
    #     # query database for current schema
    #     # take the input schema and compare them by iterating them the same where
    #     # find out what is not the same
    #     columnholder = []
    #     schema = self.session.query(models.Sheets_Schema).filter(models.Sheets_Schema.sheet_id==table_id).all()
    #
    #     for col in schema
    #         columnholder.append(DTColumn(col.id,col.column_name,col.column_type))
    #         return dtable(table_id,table_name,dt_columns)





    def get_schema(self,name):
        # tablename = name
        insp = inspect(eng)
        print(insp.get_columns(name))







#set schema takes the dtable object and the creates the connections and sets object into a schema
#     def set_schema(self,dtableobject):
#
#         # need to parse the info
#         # set the name
#         # give the table an ID
#         #
#         #receives and object and applies it to the the database
#         #compare the table to the dtable object to see if it is already in existance
#         #use the id to compare the table
#
#         #if the id is None - it is a new
#         #if there is an id
#
#
#
#         # tabletitle = request.POST.get('the_post') #this is a get to get the information from a ajax call
#
# #still needs a compare function here!!!
#             __tablename__ = dtableobject.name
#
#         Base.metadata.bind = eng
#         # The declarative Base is bound to the database engine.
#         Base.metadata.create_all()
#         # The create_all() method creates all configured tables; in our case, there is only one table from the models.
#         ses = Session()
#         # A session object is created.
#         ses.add_all(dtableobject)
#         # With the add_all() method, we add the specified instances of Car classes to the session.
#         ses.commit()
#         # The changes are committed to the database with the commit() method.
#         rs = ses.query(DTable).all()
#         # We query for all data from the Cars table. The query() method loads all instances of the Car class and its all() method returns all results represented by the query as a list.
#         for item in rs:
#             print(item.col1, item.col2)
#         # We iterate through the result set and print two columns for all returned rows.



#need to test this
    def printschema(self,table):
        for t in metadata.sorted_tables:
           print(t.name)




    class DTSchemaStoreJSON(object):
        pass





    def __repr__(self):
        return "<DTable  {} >".format(self.name)
            # prints a printable representation  of the object
