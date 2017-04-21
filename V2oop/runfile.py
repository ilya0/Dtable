import dtableapp
# import dtschemastoreapp
# _(self, id, name, internal_name, columns):



table1 = dtableapp.DTable("dtable1test")
table2 = dtableapp.DTable("dtable2test")

column1 = dtableapp.DTColumn("column1","integer")
column2 = dtableapp.DTColumn("column2","integer")

table1.add_column(column1)
table1.add_column(column2)


# table1 should look like dtable1test((column1,integer), (column2,integer))
# print(table1.get_columns())

print(table1)
