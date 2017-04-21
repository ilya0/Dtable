import dtableapp
# import dtschemastoreapp
# _(self, id, name, internal_name, columns):



table1 = dtableapp.DTable("dtable1test")
table2 = dtableapp.DTable("dtable2test")


print(table1.get_columns())
table1.printtable()
