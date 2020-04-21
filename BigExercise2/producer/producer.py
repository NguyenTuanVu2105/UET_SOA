import pika 
import sys
import os
import time

if 'AMQP_HOST' in os.environ:
   host = os.environ['AMQP_HOST']
else:
   host = 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()

channel.exchange_declare(exchange='music', exchange_type='direct')

file_song = os.path.join(os.path.dirname(os.path.abspath(__file__)).replace('/producer', ''), 'playlists.txt')
with open(file_song, 'r') as f:
   songs = f.readlines()
   for song in songs: 
      if 'zingmp3.vn' in song:
         routing_key = 'zingmp3'
      elif 'soundcloud.com' in song:
         routing_key = 'soundcloud'
      channel.basic_publish(exchange='music',
                           routing_key=routing_key,
                           body=song.strip(),
                           properties=pika.BasicProperties(
                              delivery_mode=2, 
                              expiration='60000'
                           ))
      print(" [x] Sent %r:%r" %  (routing_key, song.strip()))
connection.close()

