import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='process_status', durable=True)


def notify_success():
    channel.basic_publish(exchange='',
                          routing_key='process_status',
                          body='update_graph')
