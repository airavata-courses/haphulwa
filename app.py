#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='129.114.17.184:15672'))

channel = connection.channel()

channel.queue_declare(queue='rpc_prime_queue')

def is_prime(n):
  if n == 2 or n == 3: return 0
  if n < 2 or n%2 == 0: return 1
  if n < 9: return 0
  if n%3 == 0: return 1
  r = int(n**0.5)
  f = 5
  while f <= r:
    print('\t',f)
    if n%f == 0: return 1
    if n%(f+2) == 0: return 1
    f +=6
  return 0

def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] prime(%s)" % n)
    response = is_prime(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_prime_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
