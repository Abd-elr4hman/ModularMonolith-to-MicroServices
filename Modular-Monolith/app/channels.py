from blinker import signal
from typing import Callable

class Channel:
    def __init__(self, name:str):
        self.name = name
        self.signal = signal(self.name)
        
    def __repr__(self):
        return f'<Channel {self.name}>'
    
    def sub(self, func:Callable):
        self.signal.connect(func)

    def pub(self, sender: str , body:dict):
        self.signal.send(sender, **body)
