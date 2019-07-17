from abc import ABC, abstractmethod
from time import sleep
import ast

class Protocol(ABC):

    def __init__(self, protocol_id, protocol_type):
        self.id = protocol_id
        self.type = protocol_type
        super().__init__()

    # TODO: Wieso haben die Funktionen hier kein `self`?
    @abstractmethod
    def execute(device, action):
        pass

    @abstractmethod
    def send(*args, **kwargs):
        pass

    def wait(parameters):
        wait_time = ast.literal_eval(parameters)['sleep_time']
        sleep(wait_time)
