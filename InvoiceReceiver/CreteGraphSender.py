import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='process_status', durable=True)


def notify_success():
    print('sending message')
    channel.basic_publish(exchange='',
                          routing_key='process_status',
                          body='new data entered')
