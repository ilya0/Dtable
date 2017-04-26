import dtableapp
import dtschemastoreapp
# import dtdataengineapp # this is the data stuff, turning it off right now


#object creation from what would be the front end
def createobject(name):
    table1 = dtableapp.DTable(name)


    column1 = dtableapp.DTColumn("column1","integer")
    column2 = dtableapp.DTColumn("column2","integer")
    column3 = dtableapp.DTColumn("column3","integer")


    table1.add_column(column1)
    table1.add_column(column2)
    table1.add_column(column3)
    table1.delete_column_list(0)
    table1.delete_column_list(1)

    # table1 should look like dtable1test((column1,integer), (column2,integer))
    # print(table1.get_columns())

    return table1





# running get schema from the dtschemastore class in dtschemastoreapp
def DTSchemaStoretesting(id):

    dtschemastoreobject1 = dtschemastoreapp.dtschemastoreSQL.get_schema(id)
    print(dtschemastoreobject1)



# dtschemastoretesting(1) #not working because I need to setup IDs for tables in db
#dtschemastoretesting("dt_user_table")




#testvarschema = [{'name': 'id', 'type': "INTEGER()", 'nullable': False, 'default': 'nextval(\'"User_id_seq"\'::regclass)', 'autoincrement': True}, {'name': 'username', 'type': "VARCHAR(length=100)", 'nullable': True, 'default': None, 'autoincrement': False}, {'name': 'email', 'type': "VARCHAR(length=100)", 'nullable': True, 'default': None, 'autoincrement': False}]
#
# testarray = [{'name': 'id'}]
# print("testvar.name ======")
# print(testvarschema[0].get('name'))
# print(len(testarray))
#
#
#dtschemastoreapp.dtschemastoreSQL.compare_schema(testvarschema,testvarschema)

# {'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': 'nextval(\'"User_id_seq"\'::regclass)', 'autoincrement': True}
# {'name': 'username', 'type': VARCHAR(length=100), 'nullable': True, 'default': None, 'autoincrement': False},
# {'name': 'email', 'type': VARCHAR(length=100), 'nullable': True, 'default': None, 'autoincrement': False}


#-- to create a table --
inputname = "runfiletestabledelcolumn"


createobject(inputname)
tempobject = createobject(inputname) # create object
print(tempobject)
# set the schema from the dtable object
#DTSchemaStoreapp.DTSchemaStoreSQL.set_schema(tempobject)

# send the data in the data engine using the same object
#dtdataengineapp.dt_data_engineSQL.gen_table(dtableobject) #not working currently





# # -- drop table --
# print(inputname+ " Deleted")
# DTSchemaStoreapp.DTSchemaStoreSQL.droptable(tempobject)


# -- Delete row --


DTSchemaStoreSQL.delete_schema_column(tempobject)
