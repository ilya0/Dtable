# engine works with the data and does that actual placements in to the database
from sqlalchemy import *
print("dataengineapp loaded")

# %%%%database connections
# sqlstore = DTSchemaStoreSQL(db)
# datastore = DTDataEngineSQL(db)
eng = sqlalchemy.create_engine('postgresql+psycopg2://admin:@localhost:5432/dtabledatabase') # this is the connection to the database
meta = MetaData(eng)
# creates a meta object to hold all the things
Base = declarative_base() #declarative base class is created with this function
Session = sessionmaker(bind=eng)




#needs a method that returns a sql alchemy object

class dt_data_engine():
    pass



class DTDataEngineSQL(dt_data_engine):

    def get_data(self,table):
        pass


    #generates the table
    def gen_table(self,table):
        metadata = sqlalchemy.MetaData(self.engine)
        table = sqlalchemy.Table(
                'table_{}'.format(dtable.info['table_id']),
                metadata, sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True))
        metadata.create_all()



    def get_data(self,dtable_instance):
        #returns data object
        #    return dtabledata(dtable_instance,self)
        pass


