''' mssqlserver.py '''

import os
import pyodbc
from dotenv import load_dotenv
from os.path import join, dirname, os

''' ConnectSqlServer '''
class ConnectSqlServer:

    def __init__(self):
        ## load environment values from .env
        dotenv_path = join(dirname(__file__), '../.env')
        load_dotenv(dotenv_path)

        self.server = os.getenv("MSSQL_SERVER")
        self.database = os.getenv("MSSQL_DATABASE")
        self.driver = os.getenv("MSSQL_DRIVER")
        self.username = os.getenv("MSSQL_USERNAME")
        self.password = os.getenv("MSSQL_PASSWORD")

    '''
        connect to sql server
    '''
    def connect_sql_server(self):
        try:

            conn = pyodbc.connect(r'''DRIVER=''' + self.driver + r''';
                Server=''' + self.server + r''';
                UID=''' + self.username + r''';
                PWD=''' + self.password + r''';
                DATABASE=''' + self.database + r''';''')

            return conn

        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print("Connection Failed Error Code:" + sqlstate)
            return 0

    '''
        gets all the tables and views in the database
    '''
    def get_all_tables(self, conn):
        cursor = conn.cursor()
        tables = []
        for row in cursor.tables():
            tables.append(row.table_name)

        return tables

    '''
        basic select statement
    '''
    def get_rows_from_table(self, conn, fields, table, query =''):
        pass
