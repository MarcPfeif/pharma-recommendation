''' main.py '''

import datetime
import logging
from db import Db
from dotenv import load_dotenv
from import_drug_orders import ImportDrugOrders
from mssqlserver import ConnectSqlServer
from os.path import join, dirname, os
import pathlib


## Load .env values
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

## Setup Logging ( warning, info and debug)
logging.basicConfig(
    filename=os.getenv("PHARMA_INGEST_LOG"),
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

## connect to SQL Server Data Warehouse
sqlServer = ConnectSqlServer()
conn = sqlServer.connect_sql_server()

#tables = sqlServer.get_all_tables(conn)
#print(tables)

## no parameter <-- call generic stored procedure proc
#sqlServer.call_stored_procedure(conn, "p_PCCDrugOrderGetList")

## get drug orders for the current date
## sqlServer.get_all_drug_orders(conn)

## get drug orders for a specific date
#sqlServer.get_drug_orders_by_date(conn, '10/16/2017')

## get drug order for today
now = datetime.datetime.now()
today = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
today = "10/16/2017"
orders = sqlServer.get_drug_orders_by_date(conn, today)

## connect to postgres
db = Db()
connection = db.connect_postgres()

con = connection[0]
meta = connection[1]

## process Orders
importOrders = ImportDrugOrders(con, meta)
importOrders.process_orders(orders)
