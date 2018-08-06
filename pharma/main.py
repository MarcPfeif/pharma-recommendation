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

## connect to postgres
db = Db()
connection = db.connect_postgres()
con = connection[0]
meta = connection[1]

## get drug order for today
now = datetime.datetime.now()
today = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
orders = sqlServer.get_drug_orders_by_date(conn, today)

## process Orders
importOrders = ImportDrugOrders(con, meta)
importOrders.process_orders(orders)
