import dtableapp
import dtschemastoreapp
# _(self, id, name, internal_name, columns):
table1 = dtableapp.dtable(1,"testname","internalnametext",["test", "test2"])

print(table1.get_columns())
print(table1)
