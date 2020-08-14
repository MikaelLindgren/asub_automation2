import database_dude as dd
import pxwriter as px
table_name = 'Bruttonationalproduktperpersonochregion'
values = dd.get_values_from_table(table_name)
result = dd.get_table(table_name, "acme")

parsed_data = dd.parse_data(values, result)
px.write_VALUES(parsed_data)
px.write_meta_data()