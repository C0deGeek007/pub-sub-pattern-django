import json
from celery import shared_task
import pika
import sys
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')


@shared_task
def add(x, y):
    print("in result function")
    channel.basic_publish(exchange='logs', routing_key='', body="message for add")
    return x + y

@shared_task
def produce_permission_update_message(user):
    print("skdhbc")
    message = user
    channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(message))
    return "abc"
