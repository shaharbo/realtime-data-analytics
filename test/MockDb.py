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

    def delete_table(self):
        cur = self.conn.cursor()
        cur.execute('DROP TABLE {tn}'.format(tn='test'))
        self.conn.commit()
        if self.conn:
            self.conn.close()
