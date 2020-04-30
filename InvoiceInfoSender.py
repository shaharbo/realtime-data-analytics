import pika, json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='invoice_info', durable=True)


message = {'path': "invoices/invoices_2010.json", 'format': "json", 'loadTo': 'invoices'}
channel.basic_publish(exchange='',
                      routing_key='invoice_info',
                      body=json.dumps(message))


print(" [x] Sent %r" % message)
# connection.close()
