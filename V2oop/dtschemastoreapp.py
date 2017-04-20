import dtableapp
import models


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
        #method to set the schema after is had been decided
        #returns a dtable object
        pass



    def __repr__(self):
        return "<DTable  {} {} {}>".format(self.internal_name, self.id, self.name)
            # prints a printable representation  of the object
