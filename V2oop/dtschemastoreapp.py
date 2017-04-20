import dtableapp
import models

#creates objects of currently populated databases
#read from database to create object
#gets dtable objects to apply them to the schema and current database




#need to connect database here
# sqlstore = DTSchemaStoreSQL(db)
# datastore = DTDataEngineSQL(db)
eng = sqlalchemy.create_engine('postgresql+psycopg2://admin:@localhost:5432/dtabledatabase') # this is the connection to the database
meta = MetaData() # creates a meta object to hold all the things
Base = declarative_base() #declarative base class is created with this function




class dtschemastore(object):

    def compare_schema(self):
        columnholder = []
        schema = self.session.query(models.Sheets_Schema).filter(models.Sheets_Schema.sheet_id==table_id).all()

    for col in schema
        columnholder.append(DTColumn(col.id,col.column_name,col.column_type))
        return dtable(table_id,table_name,dt_columns)

    def get_schema(self,name):
        return(dtable(name))

    def set_schema(self):
        #receives and object and applies it to the the database
        #compare the table to the dtable object to see if it is already in existance
        #use the id to compare the table

        #if the id is None - it is a new
        #if there is an id

        # this
        pass

    def __repr__(self):
        return "<DTable  {} {} {}>".format(self.internal_name, self.id, self.name)
            # prints a printable representation  of the object
