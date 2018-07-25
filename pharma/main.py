''' main.py '''

from mssqlserver import ConnectSqlServer


sqlServer = ConnectSqlServer()

conn = sqlServer.connect_sql_server()

tables = sqlServer.get_all_tables(conn)
#print(tables)

views = sqlServer.get_all_views(conn)
print(views)
