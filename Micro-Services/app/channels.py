from typing import Callable
import pika
import json 

class Channel:
    def __init__(self, name:str):
        self.name=name
        connection_param = pika.ConnectionParameters(host='localhost')
        connection = pika.BlockingConnection(connection_param)
        self.channel = connection.channel()
        self.queue = self.channel.queue_declare(name)
        
    def __repr__(self):
        return f'<Channel {self.name}>'
    
    def sub(self, func:Callable):
        self.channel.basic_consume(queue="reports", auto_ack=True, on_message_callback=func)
        self.channel.start_consuming()

    def pub(self, sender: str, body:dict):
        body = json.dumps(body)
        self.channel.basic_publish(exchange='', routing_key=self.name, body= body)
        
