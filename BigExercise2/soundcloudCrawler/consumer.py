import os
import pika
import time
from main import downloadPlaylist
import multiprocessing


def callback(ch, method, properties, body):
    url =  body.decode('utf8')
    print(" [x] Received %r" % url)
    downloadPlaylist(url)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume():
    if 'AMQP_HOST' in os.environ:
        host = os.environ['AMQP_HOST']
    else:
        host = 'localhost'
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host, heartbeat=600, blocked_connection_timeout=3000))
    channel = connection.channel()
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', heartbeat=600, blocked_connection_timeout=3000))
    channel = connection.channel()

    channel.exchange_declare(exchange='music', exchange_type='direct', durable=False, auto_delete=False)
    result = channel.queue_declare(queue='soundcloud_queue', durable=False, exclusive=False, auto_delete=False)
    queue_name = result.method.queue
    channel.queue_bind(exchange='music', queue=queue_name, routing_key='soundcloud')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=queue_name, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


workers = 5
pool = multiprocessing.Pool(processes=workers)
for i in range(0, workers):
    pool.apply_async(consume)

try:
    while True:
        continue
except KeyboardInterrupt:
    print(' [*] Exitting')
    pool.terminate()
    pool.join()