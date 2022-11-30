import pika
from config import *


class PikaClient:

    def __init__(self) -> None:
        self.connection = None
        self.channel = None

    def connect(self):
        cred = pika.PlainCredentials(RABBIT_NAME, RABBIT_PASSWORD)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=RABBIT_HOST,
            port=int(RABBIT_PORT),
            virtual_host=RABBIT_VIRTUAL,
            credentials=cred))
        self.channel = self.connection.channel()

    def create_queue(self):
        self.channel.queue_declare(queue='hello')
    
    def send_message(self, body):
        self.connect()
        self.channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=body)

