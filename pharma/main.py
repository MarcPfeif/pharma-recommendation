''' main.py '''

import datetime
from mssqlserver import ConnectSqlServer

sqlServer = ConnectSqlServer()

conn = sqlServer.connect_sql_server()

#tables = sqlServer.get_all_tables(conn)
#print(tables)

## no parameter <-- call generic stored procedure proc
#sqlServer.call_stored_procedure(conn, "p_PCCDrugOrderGetList")

## get drug orders for the current date
## sqlServer.get_all_drug_orders(conn)

## get drug orders for a specific date
sqlServer.get_drug_orders_by_date(conn, '10/16/2017')

## get drug order for today
now = datetime.datetime.now()
today = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
today = "10/16/2017"
sqlServer.get_drug_orders_by_date(conn, today)
