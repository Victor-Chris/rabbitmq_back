import pika
import sys
import os


def main():
    connection = pika.BlockConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Ensure Queue exists
    channel.queue_declare(queue='test_queue')

    '''Call back function'''

    def callback(ch, method, properties, body):
        print(" [X] received %r" % body)

    # Subscribe callback to Queue
    channel.basic_consume(queue='test_queue', auto_ack=True,
                          on_message_callback=callback)

    # Run loop to wait for data and call callback till exited
    print(" [X] Waiting for message. To exit, press Ctrl+C")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
