import dtableapp
import dtschemastoreapp
# _(self, id, name, internal_name, columns):


# def dtabletesting():
#     table1 = dtableapp.DTable("dtable1test")
#     table2 = dtableapp.DTable("dtable2test")
#
#     column1 = dtableapp.DTColumn("column1","integer")
#     column2 = dtableapp.DTColumn("column2","integer")
#     column3 = dtableapp.DTColumn("column3","integer")
#
#
#     table1.add_column(column1)
#     table1.add_column(column2)
#     table1.add_column(column3)
#
#
#     # table1 should look like dtable1test((column1,integer), (column2,integer))
#     # print(table1.get_columns())
#
#     print(table1)
#
# #
# # dtabletesting()




def dtschemastoretesting(id):

    dtschemastoreobject1 = dtschemastoreapp.dtschemastoreSQL.get_schema(id) # running get schema from the dtschemastore class in dtschemastoreapp
    print(dtschemastoreobject1)



# dtschemastoretesting(1) #not working because I need to setup IDs for tables in db
# dtschemastoretesting("dt_user_table")






testvar = [{'name': 'id', 'type': "INTEGER()", 'nullable': False, 'default': 'nextval(\'"User_id_seq"\'::regclass)', 'autoincrement': True}, {'name': 'username', 'type': "VARCHAR(length=100)", 'nullable': True, 'default': None, 'autoincrement': False}, {'name': 'email', 'type': "VARCHAR(length=100)", 'nullable': True, 'default': None, 'autoincrement': False}]

testarray = [{'name': 'id'}]
print("testvar.name ======")
print(testvar[0].get('name'))
print(len(testarray))


dtschemastoreapp.dtschemastoreSQL.compare_schema(testvar,testvar)

# {'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': 'nextval(\'"User_id_seq"\'::regclass)', 'autoincrement': True}
# {'name': 'username', 'type': VARCHAR(length=100), 'nullable': True, 'default': None, 'autoincrement': False},
# {'name': 'email', 'type': VARCHAR(length=100), 'nullable': True, 'default': None, 'autoincrement': False}

# structure is:
# name
# type
# nullable
# default
# autoincrement
