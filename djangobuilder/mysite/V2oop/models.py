import sqlalchemy
from sqlalchemy import (
        Column, Integer, String, ForeignKey,
)

from sqlalchemy.orm import (
        mapper, relationship, backref
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class dt_user_table(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User {}>".format(self.username)

#models needs to be setup correctly with foreignkeys,



class dt_sheets(Base):
    __tablename__ = 'sheets'
    id = Column(Integer, primary_key=True)
    table_name = (varchar(100))
    user_id =  Column(Integer, ForeignKey("dt_user_table.id", ondelete='CASCADE'))
    column_name = Column(String(180), unique=True)
    column_sequence = Column(Integer)
    table_id = Column(Integer)


    def __init__(self, user_id, sheet_name):
        self.user_id = user_id
        self.sheet_name = sheet_name

    def __repr__(self):
        return "<User's:{} Sheet_Name:{}>".format(
                self.user_id,
                self.sheet_name)

class dt_data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    column_id = Column(Integer, ForeignKey("dt_sheets.id", ondelete='CASCADE'))
    row_sequence = Column(String(150))
    value = Column(String(150))
    column_name = Column(varchar(100))

    # def __init__(self, sheet, column_name, column_type, sequence_number):
    #     self.sheet = sheet
    #     self.column_name = column_name
    #     self.column_type = column_type
    #     self.sequence_number = sequence_number
    #
    # def __repr__(self):
    #     return "<Sheets_Schema {} {} {} {}>".format(
    #             self.sheet, self.column_name, self.column_type, self.sequence_number)
