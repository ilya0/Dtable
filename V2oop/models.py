import sqlalchemy
from sqlalchemy import (
        Column, Integer, String, ForeignKey,
)



from sqlalchemy.ext.declarative import declarative_base

class name(models.Model):
    name = models.CharField(max_length=200)
    #name text
    location = models.CharField(max_length=200)
    #location text
    age = models.CharField(max_length=3)
    # this is a character field defined as max length of 200
    pub_date = models.DateTimeField('date published')
    # this is an automated date stamp with the date published title
    def __str__(self):
        return self.name




Base = declarative_base()


#this is the table of users
class User(Base):

    __tablename__ = 'users'
    id = models.CharField(Integer, primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User {}>".format(self.username)



#this is a table that contains all the tables and refferences all the users
class Sheets(Base):

    __tablename__ = 'sheets'
    id = models.CharField(Integer, primary_key=True)
    user_id = models.CharField(max_length=200)
    sheet_name = models.CharField(max_length=200)

    def __init__(self, user_id, sheet_name):
        self.user_id = user_id
        self.sheet_name = sheet_name

    def __repr__(self):
        return "<User's:{} Sheet_Name:{}>".format(
                self.user_id,
                self.sheet_name)

#this is a table to create actual tables to house all the data
class Sheets_Schema(Base):

    __tablename__ = 'sheets_schema'
    id = models.CharField(Integer, primary_key=True)
    sheet_id = models.CharField(Integer, ForeignKey("sheets.id", ondelete='CASCADE'))
    sheet = relationship('Sheets',
            backref=backref('sheets_schema', lazy='dynamic', cascade='all, delete-orphan'))
    column_name = models.CharField(max_length=200, unique=True)
    column_type = models.CharField(max_length=200)

    def __init__(self, sheet, column_name, column_type):
        self.sheet = sheet
        self.column_name = column_name
        self.column_type = column_type

    def __repr__(self):
        return "<Sheets_Schema {} {} {}>".format(
                self.sheet, self.column_name, self.column_type,)
