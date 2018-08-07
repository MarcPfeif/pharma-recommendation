''' db '''
import sqlalchemy

''' Db '''
class Db:

    def connect_postgres(self, user, password, db, host='localhost', port=5432):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)

        # The return value of create_engine() is our connection object
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
        meta = sqlalchemy.MetaData(bind=con, reflect=True)

        return con, meta

    def get_all_tables(self, meta):
        for table in meta.tables:
            print(table)
