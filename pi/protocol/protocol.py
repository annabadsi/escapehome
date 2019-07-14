from abc import ABC, abstractmethod
from time import sleep

class Protocol(ABC):

    def __init__(self, protocol_id, protocol_type):
        self.id = protocol_id
        self.type = protocol_type
        super().__init__()

    @abstractmethod
    def execute(device, action):
        pass

    @abstractmethod
    def send(*args, **kwargs):
        pass
    
    def wait(wait_time):
        sleep(wait_time)
