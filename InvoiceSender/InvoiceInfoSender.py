import pika, json
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='invoice_info', durable=True)


def send_message(message):
    channel.basic_publish(exchange='',
                          routing_key='invoice_info',
                          body=json.dumps(message))
    print("Sent message - %r" % message)


def run():
    print('start sending invoices...')
    invoices = os.fsencode('invoices')
    for file in os.listdir(invoices):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            message = {'path': "invoices/{name}".format(name=filename), 'format': "csv", 'loadTo': 'invoices'}
            send_message(message)
        elif filename.endswith(".json"):
            message = {'path': "invoices/{name}".format(name=filename), 'format': "json", 'loadTo': 'invoices'}
            send_message(message)
        else:
            print('wrong invoice format')
