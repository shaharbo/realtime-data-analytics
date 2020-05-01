import sqlite3


class dbHandler:
    __instance = None

    @staticmethod
    def getInstance():
        if dbHandler.__instance is None:
            dbHandler(dbPath='invoices-db')
        return dbHandler.__instance

    def __init__(self, dbPath):
        if dbHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.path = dbPath
            dbHandler.__instance = self
            self.conn = self.connect()

    def getPath(self):
        return self.path

    def connect(self):
        try:
            conn = sqlite3.connect(self.path)
            self.conn = conn  # .cursor()
            return self.conn
        except Exception as e:
            print('connection error, {e}'.format(e=e))
            return e

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("disconnected from database")

    def select(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        rs = cur.fetchall()
        return rs

    def insert(self, query, params):
        cur = self.conn.cursor()
        cur.execute(query, params)
        self.conn.commit()
        return cur.lastrowid

    def create_table(self, name):
        cur = self.conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS {tn} (InvoiceId INTEGER, CustomerId	INTEGER,InvoiceDate datetime,BillingAddress TEXT, '
                    'BillingCity TEXT, BillingState TEXT, BillingCountry TEXT, BillingPostalCode TEXT, Total INT);'.format(tn=name))
        self.conn.commit()
