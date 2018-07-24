''' main.py '''

from mssqlserver import ConnectSqlServer


sqlServer = ConnectSqlServer()

sqlServer.connect_sql_server()
