import pika
from DbHandler import dbHandler
from GraphUtils import get_data

db = dbHandler.getInstance()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='process_status', durable=True)
print('Queue process_status is up and waiting for messages...')


def callback(ch, method, properties, body):
    print(" message Received %r" % body)
    get_data(db)


channel.basic_qos(prefetch_count=1)
channel.basic_consume('process_status', callback, auto_ack=True)
channel.start_consuming()
