from numpy.core.defchararray import lower
import json, pandas
import os.path
from Db.DbHandler import dbHandler

db = dbHandler.getInstance()


def process_message(body):
    if 'format' not in body or 'path' not in body or 'loadTo' not in body:
        print('missing one or more fields in body object')
        return False

    format = lower(body['format'])
    file = body['path']
    loadTo = body['loadTo']

    if os.path.exists(file):
        if format == 'csv':
            return load_csv_to_db(file, loadTo)
        elif format == 'json':
            return load_json_to_db(file, loadTo)
        else:
            print("error - received {0} format, invoice format must be csv or json".format(format))
            return False
    else:
        print("could not find given path")
        return False


def load_json_to_db(path, tablename):
    db.create_table(tablename)
    try:
        with open(path, encoding='utf-8-sig') as json_file:
            json_data = json.loads(json_file.read())
            query = 'insert into "{0}" values (?,?,?,?,?,?,?,?,?)'.format(tablename)
            for child in json_data:
                params = (child['InvoiceId'], child['CustomerId'], child['InvoiceDate'], child['BillingAddress'], child['BillingCity'], child['BillingState'], child['BillingCountry'], child['BillingPostalCode'], child['Total'])
                db.insert(query, params)
            json_file.close()
            print('invoices inserted successfully!')
            return True
    except Exception as e:
        print(e)
        return False


def load_csv_to_db(path, tablename):
    db.create_table(tablename)
    try:
        df = pandas.read_csv(path)
        df.to_sql(tablename, db.conn, if_exists='append', index=False)
        print('invoices inserted successfully!')
        return True
    except Exception as e:
        print(e)
        return False
