from collections import OrderedDict
import dtschemastoreapp
from sqlalchemy import Column, Integer

eng = sqlalchemy.create_engine('postgresql+psycopg2://admin:@localhost:5432/dtabledatabase') # this is the connection to the database
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
metadata = MetaData(bind=engine)

print("dtableapp imported")

class dtable(object):
    def __init__(self, id, name, internal_name, columns):
        self.id = id
        self.name = name
        self.internal_name = internal_name
        # self.columns = OrderedDict()
        self.columns = columns

    # expect DTcolumn objects
    def get_columns(self):
        columns = Sheets('savedata_name', metadata, autoload=True)
        return self.columns


    def add_columns(self,input):
        self.column = input

    def remove_column(self):
        print("remove columns hit")

    def get_tabledata(self):
        meta.reflect(bind=eng)

        for table in meta.tables:
            print(table)



    def __repr__(self):
        return "<DTable  {} {} {} {}>".format(self.internal_name, self.id, self.name, self.columns)
        # prints a printable representation  of the object




    # add a column to the dynamically generated table
    # def add_column(self,table_name, column_name, column_type):
    #     table = Table(table_name, metadata)
    #     col = sqlalchemy.Column(column_name, getattr(sa_types, column_type))
    #     col.create(table, populate_default=True)
    #
    # # def add_column(self, dt_column_object):
    # #     if not (isinstance(dt_column_object, DTColumn)):
    # #         raise Exception("invalid")
    # #     self.columns.append(dt_column_object)
