# Dtable - Dtable project is to create a airtable type app




Tech Details
------------
To run virtual enviroment - source ~/code/dyl/dtable/venv/bin/activate
source activate



PSQL commands
-------------
postgres=# \h                 # help on SQL commands
postgres=# \?                 # help on psql commands, such as \? and \h
postgres=# \l                 # list databases
postgres=# \c database_name   # connect to a database
postgres=# \d                 # list of tables
postgres=# \d table_name      # schema of a given table
postgres=# \du                # list roles
postgres=# \e                 # edit in $EDITOR



Goals for Apr 17 week
- refactor and clean up code - working
- redo code for tablelist to show all the tables in the database - finished
- change front end to be able to add columns to tables that were created
- create a selector for tables

Goals April 24 week
- Refactor database
- create schema compare methodology
    - use hard code same object to test
- create set schema method








Changes for pages
------------------

- Tablelist
    - Delete table function needs to be updated so that it works with sqlalchemy - working on delete functionality
    - Needs to pull from sqlachemy list of tables - finshed
    - buttons - edit columns and edit data need to go to the right pages

-Editcolumns page
    - Needs selector added from previous route that tell it to grab right table
    - table selector page maybe?
    - column name input box


- adddata page
    - Need table selector to which will show all the data and allow to add to
    -