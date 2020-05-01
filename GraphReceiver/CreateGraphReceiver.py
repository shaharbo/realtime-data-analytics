import pika
from Utils.GraphUtils import get_data


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='process_status', durable=True)
print('Queue process_status is up and waiting for messages...')


def callback(ch, method, properties, body):
    print(body)
    get_data()


def run():
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume('process_status', callback, auto_ack=True)
    channel.start_consuming()
