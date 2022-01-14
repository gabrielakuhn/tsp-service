import pika
from tsp_service import tsp_service

def on_message_received(ch, method, properties, body):
    response = tsp_service(body)
    #print("Message: Looking Routes for following locations", body)
    print("Response = \n ", response)


credentials = pika.PlainCredentials('admin', 'mypass')
#parameters = pika.ConnectionParameters('rabbit-server1',5672,'/',credentials)

connection_parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)# Setting same port from docker-compose file

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='inputqueue', exchange_type='fanout')

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='inputqueue', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()