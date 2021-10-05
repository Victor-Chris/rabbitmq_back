import pika

connection = pika.BlockConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure Recipient Queue exists
channel.queue_declare(queue='test_queue')

# Set up default exchange
channel.basic_publish(
    exchange='', routing_key='test_queue', body='test message...')

print(" [X] Sent test message")

# Flush network buffers
connection.close()
