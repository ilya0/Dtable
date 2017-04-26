
# works with the actual data and modifies the actual data table
class dtabledata:

    def __init__(self, schema, data_engine):
        self.schema = schema
        self.data_engine = data_engine



# these are to populate the front end

    def get_row_by_id(self,id):
        # row = self.data_engine.get_row(self.schema,id):
        row = id
        return row


    def list_row(self,id):
        pass


#set data to the database



 # tabletitle = request.POST.get('the_post') #this is a get to get the information from a ajax call


    def settabledata(self,dtableobject):
            __tablename__ = dtableobject.name

        Base.metadata.bind = eng
        # The declarative Base is bound to the database engine.
        Base.metadata.create_all()
        # The create_all() method creates all configured tables; in our case, there is only one table from the models.
        ses = Session()
        # A session object is created.
        ses.add_all(dtableobject)
        # With the add_all() method, we add the specified instances of Car classes to the session.
        ses.commit()
        # The changes are committed to the database with the commit() method.
        rs = ses.query(DTable).all()
        # We query for all data from the Cars table. The query() method loads all instances of the Car class and its all() method returns all results represented by the query as a list.
        # for item in rs:
        #     print(item.col1, item.col2)
        # # We iterate through the result set and print two columns for all returned rows.
