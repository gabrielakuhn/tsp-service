import pika
import json
import requests
from pika.exchange_type import ExchangeType

api_url = "http://127.0.0.1:8000/api/location" # Getting data from api
response = requests.get(api_url)

data = response.json()

credentials = pika.PlainCredentials('admin', 'mypass')  # Setting same credential from docker-compose file

connection_parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)  # Setting same port from docker-compose file

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='inputqueue', exchange_type=ExchangeType.fanout)

message = json.dumps(data)

channel.basic_publish(exchange='inputqueue', routing_key='', body=message)

print(f"sent message: {message}")

connection.close()