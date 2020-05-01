import json, pika
from builtins import print
from Utils.DbUtils import process_message
from InvoiceReceiver.CreteGraphSender import notify_success


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='invoice_info', durable=True)
print('Queue invoice_info is up and waiting for messages...')


def callback(ch, method, properties, body):
    print(" message Received %r" % body)
    result = process_message(json.loads(body))
    if result:
        notify_success()
    else:
        print("process message failed")


def run():
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume('invoice_info', callback, auto_ack=True)
    channel.start_consuming()
