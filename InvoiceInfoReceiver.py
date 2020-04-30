import json, pika
from builtins import print
from DbHandler import dbHandler
from DbUtils import process_message

db = dbHandler.getInstance()
conn = db.conn


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='invoice_info', durable=True)
print('Queue invoice_info is up and waiting for messages...')


connection_B = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel_B = connection_B.channel()
channel_B.queue_declare(queue='process_status', durable=True)


def notify_success():
    channel_B.basic_publish(exchange='',
                            routing_key='process_status',
                            body='new data entered')


def callback(ch, method, properties, body):
    print(" message Received %r" % body)
    result = process_message(json.loads(body), db)
    if result:
        notify_success()
    else:
        print("process message failed")


channel.basic_qos(prefetch_count=1)
channel.basic_consume('invoice_info', callback, auto_ack=True)
channel.start_consuming()
