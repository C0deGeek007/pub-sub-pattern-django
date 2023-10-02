import json
import pika
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis_connection = redis.Redis(connection_pool=pool)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    # print(f" [x] {body}")
    print("consumer")
    user = json.loads(body)
    print(user["email"])
    redis_connection.set(user["email"], body)
    value = redis_connection.get(user["email"])
    print("redis")
    print(json.loads(value))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()