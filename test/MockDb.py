import sqlite3


class MockDb:

    def __init__(self, connection_string='test_database'):
        self.conn = sqlite3.connect(connection_string)

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

## TODO: drop db after test finished
#    def clear_db(self):
