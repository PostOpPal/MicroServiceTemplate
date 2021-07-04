import pika, sys, os
from pika.adapters.blocking_connection import BlockingChannel

class Broker:
    connection: pika.BlockingConnection
    channel: BlockingChannel
    queues = {}

    def __init__(self,app):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=app.config.get("QUEUE_BROKER_URI")))
        self.channel = self.connection.channel()

    def queue(self, name):
        def wrapper(funct):
            self.queues[name] = funct
            return funct
        return wrapper

    def create_all(self):
        for queue in self.queues.keys():
            self.channel.queue_declare(queue=queue)
            self.channel.basic_consume(queue=queue, on_message_callback=self.queues[queue], auto_ack=True)

    def run(self):
        #waiting for messages 
        print("Waiting for messages")
        self.channel.start_consuming()
